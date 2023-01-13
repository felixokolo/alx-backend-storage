-- We are all unique!
-- Create a table

CREATE TABLE IF NOT EXISTS users (
  id INTEGER NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
  PRIMARY KEY (id),
  UNIQUE (email));