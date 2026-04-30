-- Lists the number of records with the same score in the table second_table
-- Displays the score and the count of records labeled as number, sorted descending
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
