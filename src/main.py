#!/usr/bin/env python3
import db_stuff as db
import data_stuff as ds
import plot_stuff as ps

DATA_FOLDER = './data/'

def setup():
    file_path = DATA_FOLDER + 'hotel_booking.csv'
    ds.learn_more_about_data(file_path)
    try:
        conn = db.connect_to_db()
        cursor = conn.cursor()
        db.init_db(cursor)
        db.load_data(cursor=cursor, file_path=file_path)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def main():
    try:
        conn = db.connect_to_db()
        cur = conn.cursor()
        print()

        # Plot bookings vs. cancellations
        ps.plot_bookings(db.get_total_bookings(cur), db.get_cancellations_rate(cur))
        print()

        # Plot average lead times
        ps.plot_avg_lead_time(db.get_avg_lead_time(cur))
        print()

        # Plot average length of stay
        ps.plot_avg_length_of_stay(db.get_avg_stay_duration(cur))
        print()

        # Plot revenue
        ps.plot_revenue(db.get_revenue_per_year(cur))
        print()

        # Plot bookings per month
        # print(db.get_booking_by_month(cur))
        ps.plot_bookings_by_season(db.get_booking_by_month(cur))
        print()

        # ps.show_plot()
    except Exception as e:
        print(e)
        return
    finally:
        conn.close()

if __name__ == "__main__":
    try:
        # setup()
        main()
    except KeyboardInterrupt:
        print('Exiting...')
        exit(0)
