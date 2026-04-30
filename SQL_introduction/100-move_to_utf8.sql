-- Converts the database, table, and name field to UTF8MB4
-- Target: Database hbtn_0c_0, Table first_table, Field name
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
