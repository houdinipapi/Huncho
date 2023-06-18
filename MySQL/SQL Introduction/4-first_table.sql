-- A script that creates a table called first_table in the current
-- database in MySQL server.
	-- first_table description:
		-- id INT
		-- name VARCHAR(256)
	-- The database name will be passed as an argument of the mysql command.
	-- If the table first_table already exists, the script should not fail.
	-- Not allowed to use the SELECT or SHOW elements.
CREATE TABLE IF NOT EXISTS `first_table` (`id` INT, `name` VARCHAR(256));
