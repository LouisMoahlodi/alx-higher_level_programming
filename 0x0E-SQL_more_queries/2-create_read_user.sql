-- This SQL command creates a new database in MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creating a new user with all privileges 
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant select privileges to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Flush all privileges to apply changes
FLUSH PRIVILEGES;
