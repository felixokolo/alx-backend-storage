-- Testing out indexing

CREATE INDEX idx_name_first ON names
(LEFT(name, 1))