-- Creating a new user with all privilages 
CREATE USER IF NOT EXISTS  'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant all privilages to the user
GRANT SELECT PRIVILEGES ON *.* TO 'user_0d_2'@'localhost'  WITH GRANT OPTION;
-- Fkush all privileges to apply changes
FLUSH PRIVILEGES;
-- This SQL commands creates a new database in my SQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;