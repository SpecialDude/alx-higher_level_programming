-- Displays Top 3 Records

SELECT city, AVG(value) AS avg_temp FROM first_table WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
