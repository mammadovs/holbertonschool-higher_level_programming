-- Displays the top 3 cities with the highest average temperatures
-- Specifically for the months of July (7) and August (8)
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
