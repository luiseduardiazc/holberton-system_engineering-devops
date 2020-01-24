CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
DROP TABLE IF EXISTS `nexus6`;
CREATE TABLE IF NOT EXISTS `nexus6` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = latin1;
INSERT INTO `nexus6` (name)
VALUES
  ('Leon');
GRANT ALL ON tyrell_corp.* TO 'holberton_user' @'localhost';
FLUSH PRIVILEGES;
SELECT
  *
FROM `nexus6`;