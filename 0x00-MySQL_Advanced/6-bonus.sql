-- Buy buy

DELIMITER $$ ;
CREATE PROCEDURE AddBonus(IN user_id_ INT,
IN project_name VARCHAR(255),
IN score_ INT)
BEGIN
DECLARE exist_pro INT;
SELECT id
INTO exist_pro
FROM projects
WHERE projects.name LIKE project_name;
IF exist_pro = NULL THEN
INSERT INTO projects (name) VALUES (project_name);
SELECT id
INTO exist_pro
FROM projects
WHERE projects.name LIKE project_name;
END IF;
INSERT INTO corrections (user_id, project_id, score)
VALUES (user_id_, exist_pro, score_);
END;$$
DELIMITER ; $$