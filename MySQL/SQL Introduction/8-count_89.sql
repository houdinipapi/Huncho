-- A script that displays the number of records with id = 89
-- in the table first_table of the database hbtn_0c_0 in MySQL server.
	-- The database name will be passe as an argument of mysql command.
SELECT COUNT(*)
FROM `first_table`
WHERE `id` = 89;
