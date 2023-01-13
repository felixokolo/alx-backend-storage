-- We are all unique!
-- fIND NUMBER 1

SELECT origin AS origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fan DESC;
