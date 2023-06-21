-- script to setup MYSQL server for project
-- create the hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- create a user on localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges to the user on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant select privileges to user on perfomance_schema db
GRANT SELECT ON perfomance_schema.* TO 'hbnb_test'@'localhost';
