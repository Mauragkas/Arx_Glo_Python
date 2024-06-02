CREATE TABLE if not exists total_bookings (
    hotel VARCHAR(255),  
    value1 INT,
    unique (hotel)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_total_bookings(
    IN p_hotel VARCHAR(255),
    IN p_value1 INT
)
BEGIN
    INSERT INTO total_bookings (hotel, value1)
    VALUES (p_hotel, p_value1)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1;
END //

DELIMITER ;

CREATE TABLE if not exists cancellations_rate (
    hotel VARCHAR(255),  
    value1 INT,
    value2 DECIMAL(10, 5),
    unique (hotel)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_cancellations_rate(
    IN p_hotel VARCHAR(255),
    IN p_value1 INT,
    IN p_value2 DECIMAL(10, 5)
)
BEGIN
    INSERT INTO cancellations_rate (hotel, value1, value2)
    VALUES (p_hotel, p_value1, p_value2)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1,
        value2 = p_value2;
END //

DELIMITER ;

CREATE TABLE if not exists avg_lead_time(
    hotel VARCHAR(255),  
    value1 DECIMAL(10, 5),
    unique (hotel)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_avg_lead_time(
    IN p_hotel VARCHAR(255),
    IN p_value1 DECIMAL(10, 5)
)
BEGIN
    INSERT INTO avg_lead_time (hotel, value1)
    VALUES (p_hotel, p_value1)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1;
END //

DELIMITER ;

CREATE TABLE if not exists avg_stay_duration(
    hotel VARCHAR(255),  
    value1 DECIMAL(10, 5),
    unique (hotel)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_avg_stay_duration(
    IN p_hotel VARCHAR(255),
    IN p_value1 DECIMAL(10, 5)
)
BEGIN
    INSERT INTO avg_stay_duration (hotel, value1)
    VALUES (p_hotel, p_value1)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1;
END //

DELIMITER ;

CREATE TABLE if not exists revenue_per_year(
    year INT,
    value1 DECIMAL,
    unique (year)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_revenue_per_year(
    IN p_year INT,
    IN p_value1 DECIMAL
)
BEGIN
    INSERT INTO revenue_per_year (year, value1)
    VALUES (p_year, p_value1)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1;
END //

DELIMITER ;

CREATE TABLE if not exists bookings_by_month(
    hotel VARCHAR(255),
    month VARCHAR(255),
    value1 INT,
    unique (hotel, month)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_bookings_by_month(
    IN p_hotel VARCHAR(255),
    IN p_month VARCHAR(255),
    IN p_value1 INT
)
BEGIN
    INSERT INTO bookings_by_month (hotel, month, value1)
    VALUES (p_hotel, p_month, p_value1)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1;
END //

DELIMITER ;

CREATE TABLE if not exists cancelled_bookings_by_month(
    hotel VARCHAR(255),
    month VARCHAR(255),
    value1 INT,
    unique (hotel, month)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_cancelled_bookings_by_month(
    IN p_hotel VARCHAR(255),
    IN p_month VARCHAR(255),
    IN p_value1 INT
)
BEGIN
    INSERT INTO cancelled_bookings_by_month (hotel, month, value1)
    VALUES (p_hotel, p_month, p_value1)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1;
END //

DELIMITER ;

CREATE TABLE if not exists market_segment_distribution(
    hotel VARCHAR(255),
    string VARCHAR(255),
    value1 INT,
    unique (hotel, string)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_market_segment_distribution(
    IN p_hotel VARCHAR(255),
    IN string VARCHAR(255),
    IN p_value1 INT
)
BEGIN
    INSERT INTO market_segment_distribution (hotel, string, value1)
    VALUES (p_hotel, string, p_value1)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1;
END //

DELIMITER ;

CREATE TABLE if not exists distribution_channel_distribution(
    hotel VARCHAR(255),
    string VARCHAR(255),
    value1 INT,
    unique (hotel, string)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_distribution_channel_distribution(
    IN p_hotel VARCHAR(255),
    IN string VARCHAR(255),
    IN p_value1 INT
)
BEGIN
    INSERT INTO distribution_channel_distribution (hotel, string, value1)
    VALUES (p_hotel, string, p_value1)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1;
END //

DELIMITER ;

CREATE TABLE if not exists nightly_stay_rates(
    hotel VARCHAR(255),
    value1 DECIMAL,
    value2 DECIMAL,
    value3 DECIMAL,
    unique (hotel)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_nightly_stay_rates(
    IN p_hotel VARCHAR(255),
    IN p_value1 DECIMAL,
    IN p_value2 DECIMAL,
    IN p_value3 DECIMAL
)
BEGIN
    INSERT INTO nightly_stay_rates (hotel, value1, value2, value3)
    VALUES (p_hotel, p_value1, p_value2, p_value3)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1,
        value2 = p_value2,
        value3 = p_value3;
END //

DELIMITER ;

CREATE TABLE if not exists room_type_preferences(
    hotel VARCHAR(255),
    string VARCHAR(255),
    value1 INT,
    unique (hotel, string)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_room_type_preferences(
    IN p_hotel VARCHAR(255),
    IN string VARCHAR(255),
    IN p_value1 INT
)
BEGIN
    INSERT INTO room_type_preferences (hotel, string, value1)
    VALUES (p_hotel, string, p_value1)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1;
END //

DELIMITER ;

CREATE TABLE if not exists meal_preferences(
    hotel VARCHAR(255),
    string VARCHAR(255),
    value1 INT,
    unique (hotel, string)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_meal_preferences(
    IN p_hotel VARCHAR(255),
    IN string VARCHAR(255),
    IN p_value1 INT
)
BEGIN
    INSERT INTO meal_preferences (hotel, string, value1)
    VALUES (p_hotel, string, p_value1)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1;
END //

DELIMITER ;

CREATE TABLE if not exists special_requests(
    hotel VARCHAR(255),
    value1 INT,
    value2 INT,
    value3 DECIMAL,
    unique (hotel, value1)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_special_requests(
    IN p_hotel VARCHAR(255),
    IN p_value1 INT,
    IN p_value2 INT,
    IN p_value3 DECIMAL
)
BEGIN
    INSERT INTO special_requests (hotel, value1, value2, value3)
    VALUES (p_hotel, p_value1, p_value2, p_value3)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1,
        value2 = p_value2,
        value3 = p_value3;
END //

DELIMITER ;

CREATE TABLE if not exists demographics(
    hotel VARCHAR(255),
    string VARCHAR(255),
    value1 INT,
    unique (hotel, string)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_demographics(
    IN p_hotel VARCHAR(255),
    IN string VARCHAR(255),
    IN p_value1 INT
)
BEGIN
    INSERT INTO demographics (hotel, string, value1)
    VALUES (p_hotel, string, p_value1)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1;
END //

DELIMITER ;

CREATE TABLE if not exists single_couple_family_group(
    hotel VARCHAR(255),
    value1 DECIMAL,
    value2 DECIMAL,
    value3 DECIMAL,
    unique (hotel)
);

DELIMITER //

CREATE PROCEDURE insert_or_update_single_couple_family_group(
    IN p_hotel VARCHAR(255),
    IN p_value1 DECIMAL,
    IN p_value2 DECIMAL,
    IN p_value3 DECIMAL
)
BEGIN
    INSERT INTO single_couple_family_group (hotel, value1, value2, value3)
    VALUES (p_hotel, p_value1, p_value2, p_value3)
    ON DUPLICATE KEY UPDATE
        value1 = p_value1,
        value2 = p_value2,
        value3 = p_value3;
END //

DELIMITER ;

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