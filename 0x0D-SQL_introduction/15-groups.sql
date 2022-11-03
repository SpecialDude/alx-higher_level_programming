-- Lists numbet of records with constraints

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
