-- Buy buy

DELIMITER $$ ;
CREATE TRIGGER email_val
AFTER UPDATE
ON users FOR EACH ROW
BEGIN
IF NEW.email != OLD.email THEN
UPDATE users SET valid_email = 0
WHERE NEW.id = users.id;
END IF;
END;$$
DELIMITER ; $$