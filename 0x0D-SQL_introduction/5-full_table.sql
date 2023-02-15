-- Show full description of the first_table table from the hbtn_0c) database
SELECT column_name, data_type, character_maxium_length, is nullable 
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_name= 'first_table' AND table_schema = 'hbtn_0c_0';
