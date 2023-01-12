-- We are all unique!
-- Create a table

CREATE TABLE IF NOT EXISTS users (
  id INTEGER NOT NULL AUTO_INCREMENT,
  email VARCHAR(255),
  name VARCHAR(255),
  PRIMARY KEY (id),
  UNIQUE (email));