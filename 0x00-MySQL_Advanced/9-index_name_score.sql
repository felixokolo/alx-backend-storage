-- Testing out indexing

CREATE INDEX idx_name_first ON names (name(1), score);