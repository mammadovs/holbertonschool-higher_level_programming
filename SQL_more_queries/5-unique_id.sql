-- Creates the table unique_id on your MySQL server
-- If the table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
