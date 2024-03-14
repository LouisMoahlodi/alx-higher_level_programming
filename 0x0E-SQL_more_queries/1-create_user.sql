-- MySQL user details
SET @username = 'user_0d_1';
SET @password = 'user_0d_1_pwd';

-- Creating a new user with all privilages 
CREATE USER IF NOT EXISTS  @username@'localhost' IDENNTIFIED BY @password;

-- Grant all privilages to the user
GRANT ALL PRIVILEGES ON *.* TO @username@'localhost'  WITH GRANT OPTION;

-- Fkush all privileges to apply changes
FLUSH PRIVILEGES;