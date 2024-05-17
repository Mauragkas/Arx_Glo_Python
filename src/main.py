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
        ps.plot_bookings_by_season(db.get_booking_by_month(cur), db.get_cancelled_booking_by_month(cur))
        print()

        # Plot market segment distribution
        ps.plot_bookings_by_market_segment(db.get_booking_market_segments(cur))
        print()

        # Plot distribution channel distribution
        ps.plot_bookings_by_distribution_channel(db.get_booking_distribution_channels(cur))
        print()

        # Plot nightly stay rates
        ps.plot_nightly_stay_rates(db.get_nightly_stay_rates(cur), db.get_mixed_stay_distributions(cur))
        print()

        # Plot room type preferences
        ps.plot_room_type_preferences(db.get_room_type_preferences(cur))
        print()

        # Plot booking status distribution
        ps.plot_meal_preferences(db.get_meal_preferences(cur))
        print()

        # Plot special requests distribution
        ps.plot_special_requests(db.get_special_requests(cur))
        print()

        # Plot demographics
        ps.plot_demographics(db.get_demographics(cur))
        print()

        # Plot Single, Couple, Family, Group
        ps.plot_single_couple_family_bookings(db.get_single_couple_family_bookings(cur))
        print()

        # ps.show_plot()
    except Exception as e:
        print(e)
        return
    finally:
        print('All done!')
        conn.close()

if __name__ == "__main__":
    try:
        # setup()
        main()
    except KeyboardInterrupt:
        print('Exiting...')
        exit(0)
