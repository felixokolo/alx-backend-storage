-- We are all unique!
-- fIND NUMBER 1

SOURCE metal_bands.sql;
SELECT origin, sum(fans) AS nb_fan
FROM metal_bands
GROUP BY origin
ORDER BY nb_fan DESC;
