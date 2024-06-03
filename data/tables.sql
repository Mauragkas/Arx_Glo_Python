CREATE DATABASE IF NOT EXISTS hotel_stuff;
USE hotel_stuff;

CREATE TABLE IF NOT EXISTS hotel_booking (
    hotel VARCHAR(255),
    is_cancelled TINYINT(1),
    lead_time INT,
    arrival_date_year INT,
    arrival_date_month set('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'),
    arrival_date_week_number INT,
    arrival_date_day_of_month INT CHECK (arrival_date_day_of_month BETWEEN 1 AND 31),
    stays_in_weekend_nights INT,
    stays_in_week_nights INT,
    adults INT,
    children INT,
    babies INT,
    meal set('HB', 'SC', 'BB', 'FB'),
    country VARCHAR(3),
    market_segment set('Offline TA/TO', 'Complementary', 'Aviation', 'Groups', 'Online TA', 'Direct', 'Corporate'),
    distribution_channel set('Corporate', 'TA/TO', 'Direct', 'GDS'),
    is_repeated_guest TINYINT(1),
    previous_cancellations INT,
    previous_bookings_not_canceled INT,
    reserved_room_type set('L', 'C', 'A', 'P', 'E', 'B', 'G', 'H', 'F', 'D'),
    assigned_room_type set('L', 'C', 'A', 'P', 'K', 'E', 'B', 'G', 'H', 'F', 'I', 'D'),
    booking_changes INT,
    deposit_type set('No Deposit', 'Refundable', 'Non Refund'),
    agent INT,
    company INT,
    days_in_waiting_list INT,
    customer_type set('Transient', 'Contract', 'Transient-Party', 'Group'),
    adr FLOAT,
    required_car_parking_spaces INT,
    total_of_special_requests INT,
    reservation_status set('Check-Out', 'Canceled', 'No-Show'),
    reservation_status_date DATE,
    name VARCHAR(50),
    email VARCHAR(50),
    phone_number VARCHAR(15),
    credit_card VARCHAR(20),
    unique (hotel, is_cancelled, arrival_date_year, arrival_date_month, arrival_date_week_number, arrival_date_day_of_month, name, email, phone_number, credit_card)
);

CREATE TABLE if not exists total_bookings (
    hotel VARCHAR(255),  
    value1 INT,
    unique (hotel)
);

CREATE TABLE if not exists cancellations_rate (
    hotel VARCHAR(255),  
    value1 INT,
    value2 DECIMAL(10, 5),
    unique (hotel)
);

CREATE TABLE if not exists avg_lead_time(
    hotel VARCHAR(255),  
    value1 DECIMAL(10, 5),
    unique (hotel)
);

CREATE TABLE if not exists avg_stay_duration(
    hotel VARCHAR(255),  
    value1 DECIMAL(10, 5),
    unique (hotel)
);

CREATE TABLE if not exists revenue_per_year(
    year INT,
    value1 DECIMAL,
    unique (year)
);

CREATE TABLE if not exists bookings_by_month(
    hotel VARCHAR(255),
    month VARCHAR(255),
    value1 INT,
    unique (hotel, month)
);

CREATE TABLE if not exists cancelled_bookings_by_month(
    hotel VARCHAR(255),
    month VARCHAR(255),
    value1 INT,
    unique (hotel, month)
);

CREATE TABLE if not exists market_segment_distribution(
    hotel VARCHAR(255),
    string VARCHAR(255),
    value1 INT,
    unique (hotel, string)
);

CREATE TABLE if not exists distribution_channel_distribution(
    hotel VARCHAR(255),
    string VARCHAR(255),
    value1 INT,
    unique (hotel, string)
);

CREATE TABLE if not exists nightly_stay_rates(
    hotel VARCHAR(255),
    value1 DECIMAL,
    value2 DECIMAL,
    value3 DECIMAL,
    unique (hotel)
);

CREATE TABLE if not exists room_type_preferences(
    hotel VARCHAR(255),
    string VARCHAR(255),
    value1 INT,
    unique (hotel, string)
);

CREATE TABLE if not exists meal_preferences(
    hotel VARCHAR(255),
    string VARCHAR(255),
    value1 INT,
    unique (hotel, string)
);

CREATE TABLE if not exists special_requests(
    hotel VARCHAR(255),
    value1 INT,
    value2 INT,
    value3 DECIMAL,
    unique (hotel, value1)
);

CREATE TABLE if not exists demographics(
    hotel VARCHAR(255),
    string VARCHAR(255),
    value1 INT,
    unique (hotel, string)
);

CREATE TABLE if not exists single_couple_family_group(
    hotel VARCHAR(255),
    value1 DECIMAL,
    value2 DECIMAL,
    value3 DECIMAL,
    unique (hotel)
);

-- DROP TABLE IF EXISTS cancellations_rate;
-- DROP TABLE IF EXISTS total_bookings;
-- DROP TABLE IF EXISTS avg_lead_time;
-- DROP TABLE IF EXISTS avg_stay_duration;
-- DROP TABLE IF EXISTS revenue_per_year;
-- DROP TABLE IF EXISTS bookings_by_month;
-- DROP TABLE IF EXISTS cancelled_bookings_by_month;
-- DROP TABLE IF EXISTS market_segment_distribution;
-- DROP TABLE IF EXISTS distribution_channel_distribution;
-- DROP TABLE IF EXISTS nightly_stay_rates;
-- DROP TABLE IF EXISTS room_type_preferences;
-- DROP TABLE IF EXISTS meal_preferences;
-- DROP TABLE IF EXISTS special_requests;
-- DROP TABLE IF EXISTS demographics;
-- DROP TABLE IF EXISTS single_couple_family_group;

-- SELECT 
--     TABLE_NAME, 
--     COLUMN_NAME, 
--     REFERENCED_TABLE_NAME,
--     REFERENCED_COLUMN_NAME
-- FROM 
--     INFORMATION_SCHEMA.KEY_COLUMN_USAGE
-- WHERE 
--     REFERENCED_TABLE_SCHEMA = 'hotel_stuff'
--     AND REFERENCED_TABLE_NAME IS NOT NULL;
