-- Creating a table with a unique default value
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 PRIMARY KEY,
	name VARCHAR(256)
);
