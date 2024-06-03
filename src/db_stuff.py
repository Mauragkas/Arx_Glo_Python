#!/usr/bin/env python3
import os
try:
    import mysql.connector
except ImportError:
    os.system('pip install mysql-connector-python')
    import mysql.connector
import json
import csv
from decimal import Decimal
from tqdm import tqdm # progress bar stuff
import re

DATA_FOLDER = './data/'

def connect_to_db() -> mysql.connector.connection.MySQLConnection:    # Load database credentials from JSON file
    with open(DATA_FOLDER + 'creds.json') as f:
        config = json.load(f)
    try:
        conn = mysql.connector.connect(**config)
        print('Connected to database.')
        return conn
    except mysql.connector.Error as e:
        print(e)
        return None

def exe_sql(cursor: mysql.connector.cursor.MySQLCursor, filename):
    try:
        with open(filename, 'r') as file:
            sql_script = file.read()

        statements = re.split(r'(DELIMITER\s+\S+)', sql_script)
        delimiter = ';'

        for part in statements:
            part = part.strip()
            if part.startswith('DELIMITER'):
                _, new_delimiter = part.split()
                delimiter = new_delimiter
            else:
                if delimiter in part:
                    sub_statements = part.split(delimiter)
                else:
                    sub_statements = [part]
                
                for statement in sub_statements:
                    statement = statement.strip()
                    if statement:
                        cursor.execute(statement)
        print(f'executed sql commands from {filename}')

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")

def init_db(cursor: mysql.connector.cursor.MySQLCursor, table_filename: str, procedure_filename: str):
    try:
        exe_sql(cursor, table_filename)
        exe_sql(cursor, procedure_filename)
        print('Database created.')
    except Exception as e:
        print(e)

def load_data(cursor: mysql.connector.cursor.MySQLCursor, file_path: str):
    total_rows = sum(1 for _ in open(file_path)) - 1  # Count total rows in the CSV file
    print(f'Total rows: {total_rows}')

    with open(file_path) as f:
        data = csv.reader(f)
        print(f'Loading data from {file_path}.')
        next(data)  # Skip header
        print('Header skipped.')

        # tqdm for the progress bar
        with tqdm(total=total_rows, desc="Loading data", unit="rows") as pbar:  
            for row in data:
                row = [None if x == "" or x == "Undefined" else x for x in row]
                placeholder = ', '.join(['%s'] * len(row))
                query = f'INSERT IGNORE INTO hotel_booking VALUES ({placeholder})'

                try:
                    cursor.execute(query, row)
                except mysql.connector.Error as e:
                    print(e)
                    print(row)
                    continue

                pbar.update(1) # Updating the progress bar  

    print('Data inserted.')

def get_length(cursor: mysql.connector.cursor.MySQLCursor) -> int:
    cursor.execute('SELECT COUNT(*) FROM hotel_booking')
    return cursor.fetchone()[0]

# Essential Booking Metrics Queries:
def get_total_bookings(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting total bookings...')
    cursor.execute('SELECT hotel, COUNT(*) AS count_of_rows FROM hotel_booking GROUP BY hotel')
    return cursor.fetchall()

def get_cancellations_rate(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting cancellations rate...')
    cursor.execute('''
        SELECT hotel, (COUNT(CASE WHEN is_cancelled = 1 THEN 1 END)) AS cancellations, (COUNT(CASE WHEN is_cancelled = 1 THEN 1 END) * 100.0 / COUNT(*)) AS cancellation_rate
        FROM hotel_booking
        GROUP BY hotel;
    ''')
    return cursor.fetchall()

def get_avg_lead_time(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting average lead time...')
    cursor.execute('''
        SELECT hotel, AVG(lead_time) AS avg_lead_time
        FROM hotel_booking 
        WHERE is_cancelled = 0
        GROUP BY hotel;
    ''')   
    return cursor.fetchall()

def get_avg_stay_duration(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting average stay duration...')
    cursor.execute('''
        SELECT hotel, AVG(stays_in_weekend_nights + stays_in_week_nights) AS avg_stay_duration
        FROM hotel_booking
        WHERE is_cancelled = 0
        GROUP BY hotel;
    ''')
    return cursor.fetchall()  

def get_nightly_stay_rates(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting nightly stay rates...')
    cursor.execute('''
        SELECT hotel, 
            (COUNT(CASE WHEN (stays_in_weekend_nights = 0 AND stays_in_week_nights > 0) THEN 1 END) * 100.0 / COUNT(*)) AS week_nights_rate,
            (COUNT(CASE WHEN (stays_in_weekend_nights > 0 AND stays_in_week_nights = 0) THEN 1 END) * 100.0 / COUNT(*)) AS weekend_nights_rate,
            (COUNT(CASE WHEN (stays_in_weekend_nights > 0 AND stays_in_week_nights > 0) THEN 1 END) * 100.0 / COUNT(*)) AS both_nights_rate
        FROM hotel_booking
        WHERE is_cancelled = 0
        GROUP BY hotel;
    ''')
    return cursor.fetchall()

def get_mixed_stay_distributions(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting mixed stay distributions...')
    cursor.execute('''
        WITH total_mixed_bookings AS (
            SELECT COUNT(*) AS total_count
            FROM hotel_booking
            WHERE is_cancelled = 0 
                AND stays_in_weekend_nights > 0 
                AND stays_in_week_nights > 0
        )
        SELECT
            (COUNT(CASE WHEN stays_in_weekend_nights = 1 AND stays_in_week_nights > 0 THEN 1 END) * 100.0 / total_count) AS mix_1,
            (COUNT(CASE WHEN stays_in_weekend_nights = 2 AND stays_in_week_nights > 0 THEN 1 END) * 100.0 / total_count) AS mix_2,
            (COUNT(CASE WHEN stays_in_weekend_nights > 2 AND stays_in_week_nights > 0 THEN 1 END) * 100.0 / total_count) AS mix_3
        FROM hotel_booking, total_mixed_bookings
        WHERE is_cancelled = 0;

    ''')
    return cursor.fetchall()

def get_revenue_per_year(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting revenue per year...')
    cursor.execute('''
        SELECT arrival_date_year, ROUND(SUM(adr * (stays_in_weekend_nights + stays_in_week_nights)), 2) AS revenue
        FROM hotel_booking
        WHERE is_cancelled = 0
        GROUP BY arrival_date_year;
    ''')
    return cursor.fetchall()

def get_repeat_guests(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting repeat guests...')
    cursor.execute('''
        SELECT hotel,
               (COUNT(CASE WHEN is_repeated_guest = 1 THEN 1 END) * 100.0 / COUNT(*)) AS repeat_guest_rate
        FROM hotel_booking
        WHERE is_cancelled = 0
        GROUP BY hotel;
    ''')
    return cursor.fetchall()

# Booking Patterns:
def get_booking_by_month(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting booking by month...')
    cursor.execute('''
        SELECT hotel, arrival_date_month, COUNT(*) AS count_of_rows
        FROM hotel_booking
        # WHERE is_cancelled = 0
        GROUP BY hotel, arrival_date_month;
    ''')
    return cursor.fetchall()

def get_cancelled_booking_by_month(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting cancelled booking by month...')
    cursor.execute('''
        SELECT hotel, arrival_date_month, COUNT(*) AS count_of_rows
        FROM hotel_booking
        WHERE is_cancelled = 1
        GROUP BY hotel, arrival_date_month;
    ''')
    return cursor.fetchall()

def get_booking_market_segments(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting booking market segments...')
    cursor.execute('''
        SELECT hotel, market_segment, COUNT(*) AS count_of_rows
        FROM hotel_booking
        WHERE is_cancelled = 0
        GROUP BY hotel, market_segment;
    ''')
    return cursor.fetchall()

def get_booking_distribution_channels(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting booking distribution channels...')
    cursor.execute('''
        SELECT hotel, distribution_channel, COUNT(*) AS count_of_rows
        FROM hotel_booking
        WHERE is_cancelled = 0
        GROUP BY hotel, distribution_channel;
    ''')
    return cursor.fetchall()

# Additional Insights:
def get_room_type_preferences(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting room type preferences...')
    cursor.execute('''
        SELECT hotel, reserved_room_type, COUNT(*) AS count_of_rows
        FROM hotel_booking
        WHERE is_cancelled = 0
        GROUP BY hotel, FIELD(reserved_room_type, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'P')
    ''')
    return cursor.fetchall()

def get_meal_preferences(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting meal preferences...')
    cursor.execute('''
        SELECT hotel, meal, COUNT(*) AS count_of_rows
        FROM hotel_booking
        WHERE is_cancelled = 0
        GROUP BY hotel, meal;
    ''')
    return cursor.fetchall()

def get_special_requests(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting special requests...')
    cursor.execute('''
        SELECT hotel, total_of_special_requests, COUNT(*) AS count_of_rows,
               (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM hotel_booking WHERE is_cancelled = 0)) AS percentage
        FROM hotel_booking
        WHERE is_cancelled = 0
        GROUP BY hotel, total_of_special_requests;
    ''')
    return cursor.fetchall()

def get_demographics(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting demographics...')
    cursor.execute('''
        SELECT hotel, customer_type, COUNT(*) AS count_of_rows
        FROM hotel_booking
        WHERE is_cancelled = 0
        GROUP BY hotel, customer_type;
    ''')
    return cursor.fetchall()

def get_single_couple_family_bookings(cursor: mysql.connector.cursor.MySQLCursor) -> list:
    print('Getting single, couple, family bookings...')
    cursor.execute('''
        SELECT hotel,
            (COUNT(CASE WHEN adults > 0 AND (children > 0 or babies > 0) THEN 1 END) * 100.0 / COUNT(*)) AS family_rate,
            (COUNT(CASE WHEN adults = 1 AND (children = 0 and babies = 0) THEN 1 END) * 100.0 / COUNT(*)) AS single_rate,
            (COUNT(CASE WHEN adults = 2 AND (children = 0 and babies = 0) THEN 1 END) * 100.0 / COUNT(*)) AS couple_rate
        FROM hotel_booking
        WHERE is_cancelled = 0
        GROUP BY hotel;
    ''')
    return cursor.fetchall()

def insert_into_table(cursor: mysql.connector.cursor.MySQLCursor, conn: mysql.connector.connection.MySQLConnection, table: str, data: list):
    for row in data:
        row_values = []
        for item in row:
            if isinstance(item, set):
                row_values.append(','.join(item))  # Convert sets to comma-separated strings
            elif isinstance(item, Decimal):
                row_values.append(float(item))  # Convert Decimal to float
            else:
                row_values.append(item) 
        
        placeholders = ', '.join(['%s'] * len(row_values))  # Create placeholders
        procedure_name = f"insert_or_update_{table}"  # Construct the procedure name
        query = f"CALL {procedure_name}({placeholders})"  # Construct the query

        try:
            # print(row_values)
            cursor.execute(query, row_values)
        except mysql.connector.Error as e:
            print(f"\033[91mError inserting row: {e}\033[0m")
            print(row_values)
    conn.commit()  # Commit changes to the database
    print(f'Data inserted into {table}.')

