-- creaates a user table with the following requirements
-- id (never NULL), email( 255 char string, never NULL and unique), name
-- country(enumeration)

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(500) NOT NULL UNIQUE,
    name VARCHAR(500),
    country ENUM('US', 'CO', 'TN')DEFAULT 'US'
)
