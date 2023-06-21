-- create db hbnb_dev_db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create the user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant user privileges on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant user privileges on perfomance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
