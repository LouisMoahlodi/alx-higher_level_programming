-- Creating a new user with all privilages 
CREATE USER IF NOT EXISTS  'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privilages to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'  WITH GRANT OPTION;
-- Fkush all privileges to apply changes
FLUSH PRIVILEGES;