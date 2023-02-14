-- Creates table second_table and adds multiple rows
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
-- Insert record 1
INSERT INTO second_table
VALUES (1, "John", 10);
-- Insert record 2
INSERT INTO second_table
VALUES (2, "Alex", 3);
-- Insert record 3
INSERT INTO second_table
VALUES (3, "Bob", 14);
-- Insert record 4
INSERT INTO second_table
VALUES (4, "George", 8);
