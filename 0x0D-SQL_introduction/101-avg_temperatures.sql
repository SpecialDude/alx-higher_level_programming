-- File Imports

SET autocommit=0;
source temperatures.sql;
COMMIT;

SELECT city, AVG(value) FROM temperatures GROUP BY city ORDER BY value;
