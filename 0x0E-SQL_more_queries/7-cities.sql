-- This SQL command creates a new database and table in the created database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT, FOREIGN KEY (state_id) REFERENCES states(id),
    name VARCHAR(256)
    );