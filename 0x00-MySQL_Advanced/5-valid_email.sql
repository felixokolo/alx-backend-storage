-- Buy buy

DELIMITER $$ ;
CREATE TRIGGER email_val
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
DECLARE old_email VARCHAR(255);
SELECT email
INTO old_email
FROM users
WHERE NEW.id = users.id;
IF STRCMP(NEW.email, old_email) != 0  THEN
SET NEW.valid_email = 0;
END IF;
END;$$
DELIMITER ; $$