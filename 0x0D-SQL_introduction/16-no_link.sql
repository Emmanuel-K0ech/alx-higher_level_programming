-- List all record of the table second_table
-- Dont list rows without a name value
SELECT * FROM second_table
WHERE name IS NOT NULL;
