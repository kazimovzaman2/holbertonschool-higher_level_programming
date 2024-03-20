-- ID can't be null
CREATE TABLE IF NOT EXISTS `id_not_null` (
  id INT DEFAULT 1 NOT NULL
  name VARCHAR(256) NOT NULL
);
