import csv
import json
from decimal import Decimal 

DATA_FOLDER = './data/'
CSV_FILE_FOLDER = './csv_files/'

def try_convert_type(value):
    if not value:
        return None

    try:
        return int(value)  # Try converting to integer
    except ValueError:
        try:
            return float(value)  # Try converting to float
        except ValueError:
            return str(value)  # If all else fails, keep as a string
        
def learn_more_about_data(file_path: str):
    # read the csv file
    data = csv.reader(open(file_path, 'r'))
    # skip the header
    header = next(data)

    print('Data types and values for each column:')
    # keep track of the data types of each column
    data_types_and_set = []
    for i in range(36): # 36 columns in the csv file
        data_types_and_set.append({'types': set(), 'set': set()})
    for row in data:
        for i in range(36):
            data_types_and_set[i]['types'].add(type(try_convert_type(row[i])))
            data_types_and_set[i]['set'].add(str(row[i]))
            
    with open(DATA_FOLDER + 'data_types.txt', 'w') as f:
        for i in range(36):
            if len(data_types_and_set[i]['set']) > 12:
                data_types_and_set[i]['set'] = 'NOT A SET'
            f.write(f'{header[i]}: {data_types_and_set[i]}\n')
    print('Data types written to data_types.txt')

def save_as_csv(filename, args: list):
    file_path = CSV_FILE_FOLDER + filename
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for arg in args:
            for tup in arg:
                modified_row = list(tup)  # Convert tuple to a list
                for i, item in enumerate(modified_row):
                    if isinstance(item, set):  # Safer type check
                        modified_row[i] = ', '.join(item)  # Convert set to string correctly
                    elif isinstance(item, Decimal):
                        modified_row[i] = float(item)  # Convert Decimal to float
                writer.writerow(modified_row)
    print('\033[92m' + f'CSV file saved as {file_path}' + '\033[0m')  # Show full path in case of issues
