CREATE USER IF NOT EXISTS 'replica_user' @'%' IDENTIFIED BY 'replica';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user' @'%' IDENTIFIED BY 'replica';
GRANT
SELECT
  ON mysql.user TO 'holberton_user' @'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'replica_user' @'%';
SELECT
  user,
  Repl_slave_priv
FROM mysql.user;
