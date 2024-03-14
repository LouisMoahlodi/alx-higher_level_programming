-- This SQL command creates a new database in MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
-- This SQl command creates the table in the created database
CREATE TABLE IF NOT EXISTS 'hbtn_0d_usa'.'states' (
    'id' INT(1) AUTO_INCREMENT  PRIMARY KEY, 
    'name' VARCHAR(256)
);