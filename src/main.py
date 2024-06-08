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
    print('-' * 50)
except Exception as e:
    print(e)
    exit(1)

def setup():
    ds.learn_more_about_data(file_path)
    print('-' * 50)
    try:
        # db.init_db(cur)
        db.init_db(cur, DATA_FOLDER + 'tables.sql', DATA_FOLDER + 'procedures.sql')
        print('-' * 50)
        db.load_data(cursor=cur, file_path=file_path)
        conn.commit()
        # print('-' * 50)
    except Exception as e:
        print(e)

def test():
    # arg1 = db.get_booking_by_month(cur)
    arg1 = db.get_nightly_stay_rates(cur)
    print(arg1)

def main():
    print('-' * 50)

    db.select_db(cur, 'hotel_stuff')

    plot_buttons = {
        'Bookings vs. Cancellations': lambda: (
            arg1 := db.get_total_bookings(cur),
            arg2 := db.get_cancellations_rate(cur),
            print(f'{arg1}\n{arg2}'),
            ds.save_as_csv('bookings_vs_cancellations.csv', [arg1, arg2]),
            db.insert_into_table(cur, conn, 'total_bookings', arg1),
            db.insert_into_table(cur, conn, 'cancellations_rate', arg2),
            ps.plot_bookings(arg1, arg2),
        ),
        'Average Lead Time': lambda: (
            arg1 := db.get_avg_lead_time(cur),
            print(arg1),
            ds.save_as_csv('average_lead_time.csv', [arg1]),
            db.insert_into_table(cur, conn, 'avg_lead_time', arg1),
            ps.plot_avg_lead_time(arg1),
        ),
        'Average Length of Stay': lambda: (
            arg1 := db.get_avg_stay_duration(cur),
            print(arg1),
            ds.save_as_csv('average_length_of_stay.csv', [arg1]),
            db.insert_into_table(cur, conn, 'avg_stay_duration', arg1),
            ps.plot_avg_length_of_stay(arg1),
        ),
        'Revenue': lambda: (
            arg1 := db.get_revenue_per_year(cur),
            print(arg1),
            ds.save_as_csv('revenue.csv', [arg1]),
            db.insert_into_table(cur, conn, 'revenue_per_year', arg1),
            ps.plot_revenue(arg1),
        ),
        'Bookings by Season': lambda: (
            arg1 := db.get_booking_by_month(cur),
            arg2 := db.get_cancelled_booking_by_month(cur),
            print(f'{arg1}\n{arg2}'),
            ds.save_as_csv('bookings_by_season.csv', [arg1, arg2]),
            db.insert_into_table(cur, conn, 'bookings_by_month', arg1),
            db.insert_into_table(cur, conn, 'cancelled_bookings_by_month', arg2),
            ps.plot_bookings_by_season(arg1, arg2),
        ),
        'Market Segment Distribution': lambda: (
            arg1 := db.get_booking_market_segments(cur),
            print(arg1),
            ds.save_as_csv('market_segment_distribution.csv', [arg1]),
            db.insert_into_table(cur, conn, 'market_segment_distribution', arg1),
            ps.plot_bookings_by_market_segment(arg1),
        ),
        'Distribution Channel Distribution': lambda: (
            arg1 := db.get_booking_distribution_channels(cur),
            print(arg1),
            ds.save_as_csv('distribution_channel_distribution.csv', [arg1]),
            db.insert_into_table(cur, conn, 'distribution_channel_distribution', arg1),
            ps.plot_bookings_by_distribution_channel(arg1),
        ),
        'Nightly Stay Rates': lambda: (
            arg1 := db.get_nightly_stay_rates(cur),
            arg2 := db.get_mixed_stay_distributions(cur),
            print(f'{arg1}\n{arg2}'),
            ds.save_as_csv('nightly_stay_rates.csv', [arg1, arg2]),
            db.insert_into_table(cur, conn, 'nightly_stay_rates', arg1),
            # db.insert_into_table(cur, conn, 'mixed_stay_distributions', arg2), # einai περιτο. 3 floats den aksizei na mpoun se table
            ps.plot_nightly_stay_rates(arg1, arg2),
        ),
        'Room Type Preferences': lambda: (
            arg1 := db.get_room_type_preferences(cur),
            print(arg1),
            ds.save_as_csv('room_type_preferences.csv', [arg1]),
            db.insert_into_table(cur, conn, 'room_type_preferences', arg1),
            ps.plot_room_type_preferences(arg1),
        ),
        'Meal Preferences': lambda: (
            arg1 := db.get_meal_preferences(cur),
            print(arg1),
            ds.save_as_csv('meal_preferences.csv', [arg1]),
            db.insert_into_table(cur, conn, 'meal_preferences', arg1),
            ps.plot_meal_preferences(arg1),
        ),
        'Special Requests': lambda: (
            arg1 := db.get_special_requests(cur),
            print(arg1),
            ds.save_as_csv('special_requests.csv', [arg1]),
            db.insert_into_table(cur, conn, 'special_requests', arg1),
            ps.plot_special_requests(arg1),
        ),
        'Demographics': lambda: (
            arg1 := db.get_demographics(cur),
            print(arg1),
            ds.save_as_csv('demographics.csv', [arg1]),
            db.insert_into_table(cur, conn, 'demographics', arg1),
            ps.plot_demographics(arg1),
        ),
        'Single, Couple, Family, Group': lambda: (
            arg1 := db.get_single_couple_family_bookings(cur),
            print(arg1),
            ds.save_as_csv('single_couple_family_group.csv', [arg1]),
            db.insert_into_table(cur, conn, 'single_couple_family_group', arg1),
            ps.plot_single_couple_family_bookings(arg1),
        ),
    }

    gui.window(plot_buttons)

if __name__ == "__main__":
    try:
        # if a file named .setupIsDone exists, skip setup
        with open('.setupIsDone', 'r') as f:
            print('Setup is already done')
    except FileNotFoundError:
        setup()
        with open('.setupIsDone', 'w') as f:
            pass
    try:
        main()
        # test()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        exit(0)
    finally:
        conn.close()
