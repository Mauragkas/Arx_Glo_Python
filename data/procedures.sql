DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_total_bookings(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_cancellations_rate(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_avg_lead_time(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_avg_stay_duration(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_revenue_per_year(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_bookings_by_month(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_cancelled_bookings_by_month(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_market_segment_distribution(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_distribution_channel_distribution(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_nightly_stay_rates(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_room_type_preferences(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_meal_preferences(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_special_requests(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_demographics(
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

DELIMITER //

CREATE PROCEDURE IF NOT EXISTS insert_or_update_single_couple_family_group(
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
