-- create database hbnb_test_db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create the user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant privileges to user on hbnb_test db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant user privileges on perfomance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
