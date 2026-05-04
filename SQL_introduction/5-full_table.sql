-- Description of first_table
SELECT COLUMN_NAME, COLUMN_TYPE
FROM information_schema.COLUMNS
WHERE TABLE_NAME = 'first_table'
AND TABLE_SCHEMA = DATABASE();
