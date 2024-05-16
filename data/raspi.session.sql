-- SELECT hotel, (COUNT(CASE WHEN is_cancelled = 1 THEN 1 END)) AS cancellations, (COUNT(CASE WHEN is_cancelled = 1 THEN 1 END) * 100.0 / COUNT(*)) AS cancellation_rate
-- FROM hotel_booking
-- GROUP BY hotel;

-- SELECT lead_time, COUNT(*) AS count_of_rows FROM hotel_booking 
-- where is_cancelled = 0 GROUP BY lead_time;

-- SELECT hotel, AVG(lead_time) AS avg_lead_time
--         FROM hotel_booking 
--         WHERE is_cancelled = 0
--         GROUP BY hotel;

-- SELECT hotel, AVG(stays_in_weekend_nights + stays_in_week_nights) AS avg_length_of_stay
--         FROM hotel_booking 
--         WHERE is_cancelled = 0
--         GROUP BY hotel;

-- SHOW create table hotel_booking;

-- SELECT hotel, 
--        (COUNT(CASE WHEN (stays_in_weekend_nights = 0 AND stays_in_week_nights > 0) THEN 1 END) * 100.0 / COUNT(*)) AS week_nights_rate,
--        (COUNT(CASE WHEN (stays_in_weekend_nights > 0 AND stays_in_week_nights = 0) THEN 1 END) * 100.0 / COUNT(*)) AS weekend_nights_rate,
--        (COUNT(CASE WHEN (stays_in_weekend_nights > 0 AND stays_in_week_nights > 0) THEN 1 END) * 100.0 / COUNT(*)) AS both_nights_rate
-- FROM hotel_booking
-- WHERE is_cancelled = 0
-- GROUP BY hotel;

-- WITH total_mixed_bookings AS (
--     SELECT COUNT(*) AS total_count
--     FROM hotel_booking
--     WHERE is_cancelled = 0 
--         AND stays_in_weekend_nights > 0 
--         AND stays_in_week_nights > 0
-- )
-- SELECT
--     (COUNT(CASE WHEN stays_in_weekend_nights = 1 AND stays_in_week_nights > 0 THEN 1 END) * 100.0 / total_count) AS mix_1,
--     (COUNT(CASE WHEN stays_in_weekend_nights = 2 AND stays_in_week_nights > 0 THEN 1 END) * 100.0 / total_count) AS mix_2,
--     (COUNT(CASE WHEN stays_in_weekend_nights > 2 AND stays_in_week_nights > 0 THEN 1 END) * 100.0 / total_count) AS mix_3
-- FROM hotel_booking, total_mixed_bookings
-- WHERE is_cancelled = 0;

-- SELECT arrival_date_year, ROUND(SUM(adr), 2) AS total_revenue
-- FROM hotel_booking
-- WHERE is_cancelled = 0
-- GROUP BY arrival_date_year;

-- SELECT adr from hotel_booking where is_cancelled = 0 and adr > 0 order by adr ASC;

-- SELECT arrival_date_year, ROUND(SUM(adr * (stays_in_weekend_nights + stays_in_week_nights)), 2) AS revenue
--         FROM hotel_booking
--         WHERE is_cancelled = 0
--         GROUP BY arrival_date_year;

-- SELECT hotel,
--        (COUNT(CASE WHEN is_repeated_guest = 1 THEN 1 END) * 100.0 / COUNT(*)) AS repeat_guest_rate
-- FROM hotel_booking
-- WHERE is_cancelled = 0
-- GROUP BY hotel;

-- SELECT hotel, arrival_date_month, COUNT(*) AS count_of_rows
--         FROM hotel_booking
--         WHERE is_cancelled = 0
--         GROUP BY hotel, arrival_date_month;

-- SELECT hotel, market_segment, COUNT(*) AS count_of_rows
--         FROM hotel_booking
--         WHERE is_cancelled = 0
--         GROUP BY hotel, market_segment;

-- SELECT hotel, distribution_channel, COUNT(*) AS count_of_rows
--         FROM hotel_booking
--         WHERE is_cancelled = 0
--         GROUP BY hotel, distribution_channel;

-- SELECT hotel, reserved_room_type, COUNT(*) AS count_of_rows
--         FROM hotel_booking
--         WHERE is_cancelled = 0
--         GROUP BY hotel, FIELD(reserved_room_type, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'P')

-- NA TO KSANA DOOOO AUTO
-- SELECT hotel, reserved_room_type, COUNT(*) AS bookings
-- FROM hotel_booking
-- WHERE is_cancelled = 0
-- GROUP BY hotel, reserved_room_type;

-- SELECT hotel, reserved_room_type, assigned_room_type, COUNT(*) AS bookings
-- FROM hotel_booking
-- WHERE is_cancelled = 0
-- AND reserved_room_type != assigned_room_type
-- GROUP BY hotel, reserved_room_type, assigned_room_type;

-- SELECT hotel, meal, COUNT(*) AS count_of_rows
--         FROM hotel_booking
--         WHERE is_cancelled = 0
--         GROUP BY hotel, meal;

-- SELECT hotel, total_of_special_requests, COUNT(*) AS count_of_rows,
--        (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM hotel_booking WHERE is_cancelled = 0)) AS percentage
-- FROM hotel_booking
-- WHERE is_cancelled = 0
-- GROUP BY hotel, total_of_special_requests;

-- SELECT hotel, days_in_waiting_list, COUNT(*) AS count_of_rows
--         FROM hotel_booking
--         WHERE is_cancelled = 0
--         GROUP BY hotel, days_in_waiting_list;
-- SELECT hotel, customer_type, COUNT(*) AS count_of_rows
--         FROM hotel_booking
--         WHERE is_cancelled = 0
--         GROUP BY hotel, customer_type;

-- SELECT hotel,
--     (COUNT(CASE WHEN adults > 0 AND (children > 0 or babies > 0) THEN 1 END) * 100.0 / COUNT(*)) AS family_rate,
--     (COUNT(CASE WHEN adults = 1 AND (children = 0 and babies = 0) THEN 1 END) * 100.0 / COUNT(*)) AS single_rate,
--     (COUNT(CASE WHEN adults = 2 AND (children = 0 and babies = 0) THEN 1 END) * 100.0 / COUNT(*)) AS couple_rate
-- FROM hotel_booking
-- WHERE is_cancelled = 0
-- GROUP BY hotel;
