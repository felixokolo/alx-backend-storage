-- Buy buy

DELIMITER $$
CREATE TRIGGER IF NOT EXISTS reduce
AFTER INSERT
ON orders FOR EACH ROW
BEGIN
DECLARE old_quant INT;
SELECT quantity
INTO old_quant
FROM items
WHERE NEW.item_name = items.name;
UPDATE items SET quantity = (old_quant - NEW.number)
WHERE NEW.item_name = items.name;
END;$$
DELIMITER ; $$