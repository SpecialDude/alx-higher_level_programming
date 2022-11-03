-- File Imports

SET autocommit=0;
source temperatures.sql;
COMMIT;

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY value;
