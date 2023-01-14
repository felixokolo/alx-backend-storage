-- Buy buy

DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id_ INT)
BEGIN
DECLARE avg_sc INT;
SELECT AVG(score)
INTO avg_sc
FROM corrections
WHERE corrections.user_id = user_id_;
UPDATE users SET average_score = avg_sc
WHERE users.id = user_id_;
END;$$
DELIMITER ; $$