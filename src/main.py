#!/usr/bin/env python3
import db_stuff as db
import data_stuff as ds
import plot_stuff as ps
import gui_stuff as gui

DATA_FOLDER = './data/'
file_path = DATA_FOLDER + 'hotel_booking.csv'

try:
    conn = db.connect_to_db()
    cur = conn.cursor()
except Exception as e:
    print(e)
    exit(1)

def setup():
    ds.learn_more_about_data(file_path)
    try:
        db.init_db(cur)
        db.load_data(cursor=cur, file_path=file_path)
        conn.commit()
    except Exception as e:
        print(e)

def main():
    print('-' * 50)

    plot_buttons = {
        'Bookings vs. Cancellations': lambda: (
            arg1 := db.get_total_bookings(cur),
            arg2 := db.get_cancellations_rate(cur),
            print(f'{arg1}\n{arg2}'),
            ps.plot_bookings(arg1, arg2)
        ),
        'Average Lead Time': lambda: (
            arg1 := db.get_avg_lead_time(cur),
            print(arg1),
            ps.plot_avg_lead_time(arg1)
        ),
        'Average Length of Stay': lambda: (
            arg1 := db.get_avg_stay_duration(cur),
            print(arg1),
            ps.plot_avg_length_of_stay(arg1)
        ),
        'Revenue': lambda: (
            arg1 := db.get_revenue_per_year(cur),
            print(arg1),
            ps.plot_revenue(arg1)
        ),
        'Bookings by Season': lambda: (
            arg1 := db.get_booking_by_month(cur),
            arg2 := db.get_cancelled_booking_by_month(cur),
            print(f'{arg1}\n{arg2}'),
            ps.plot_bookings_by_season(arg1, arg2)
        ),
        'Market Segment Distribution': lambda: (
            arg1 := db.get_booking_market_segments(cur),
            print(arg1),
            ps.plot_bookings_by_market_segment(arg1)
        ),
        'Distribution Channel Distribution': lambda: (
            arg1 := db.get_booking_distribution_channels(cur),
            print(arg1),
            ps.plot_bookings_by_distribution_channel(arg1)
        ),
        'Nightly Stay Rates': lambda: (
            arg1 := db.get_nightly_stay_rates(cur),
            arg2 := db.get_mixed_stay_distributions(cur),
            print(f'{arg1}\n{arg2}'),
            ps.plot_nightly_stay_rates(arg1, arg2)
        ),
        'Room Type Preferences': lambda: (
            arg1 := db.get_room_type_preferences(cur),
            print(arg1),
            ps.plot_room_type_preferences(arg1)
        ),
        'Meal Preferences': lambda: (
            arg1 := db.get_meal_preferences(cur),
            print(arg1),
            ps.plot_meal_preferences(arg1)
        ),
        'Special Requests': lambda: (
            arg1 := db.get_special_requests(cur),
            print(arg1),
            ps.plot_special_requests(arg1)
        ),
        'Demographics': lambda: (
            arg1 := db.get_demographics(cur),
            print(arg1),
            ps.plot_demographics(arg1)
        ),
        'Single, Couple, Family, Group': lambda: (
            arg1 := db.get_single_couple_family_bookings(cur),
            print(arg1),
            ps.plot_single_couple_family_bookings(arg1)
        ),
    }

    gui.window(plot_buttons)

if __name__ == "__main__":
    try:
        # setup()
        main()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        exit(0)
    finally:
        conn.close()
