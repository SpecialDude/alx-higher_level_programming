-- Lists numbet of records with constraints

SELECT score, COUNT(*) FROM second_table GROUP BY score ORDER BY score DESC;
