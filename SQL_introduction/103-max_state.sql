-- Displays the maximum temperature of each state
-- Results are ordered by State name (ascending)
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
