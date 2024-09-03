
-- Steps to recreate loading a large csv/txt file:
-- 1) Pull file from s3 to local server with aws command:
--aws s3 cp "s3://some_path/file_name.txt" "/data/local_folder/folder_name"

-- 1) Manually create the empty table.
-- 2) Run the copy command on the server tied to the database that needs to be loaded.

analyze schema_name.table_name;

-- record count.
select count(*)
from schema_name.table_name;

-- load file.
copy schema_name.table_name
from '/data/local_folder/folder_name/table_name.txt'
with CSV
HEADER
delimiter '|'
QUOTE E'\b'
;
