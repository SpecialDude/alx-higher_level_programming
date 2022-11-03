-- Displays Top 3 Records

SELECT city, AVG(value) AS avg_temp FROM first_table GROUP BY city ORDER BY avg_temp LIMIT 3;
