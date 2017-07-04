DROP TABLE IF EXISTS commands;
DROP TABLE IF EXISTS permits;

/*
  Command Table - stores the static command responses
*/
CREATE TABLE commands(
  id INT AUTO_INCREMENT NOT NULL,
  command VARCHAR(80) UNIQUE NOT NULL,
  role VARCHAR(10) NOT NULL,
  response VARCHAR(80) NOT NULL,
  lastUsed TIMESTAMP NULL,
  PRIMARY KEY(id)
);

/*TODO insert some existing commands to test with*/
INSERT INTO commands(command, role, response) VALUES("!testCmdExisting", "Mod","TEST FOR EXISTING COMMAND STUFF");

INSERT INTO commands(command, role, response) VALUES("!testRemoveExisting1", "Mod","TEST FOR EXISTING COMMAND STUFF");
INSERT INTO commands(command, role, response) VALUES("!testRemoveExisting2", "Mod","TEST FOR EXISTING COMMAND STUFF");
INSERT INTO commands(command, role, response) VALUES("!testRemoveExisting3", "Mod","TEST FOR EXISTING COMMAND STUFF");
INSERT INTO commands(command, role, response) VALUES("!testRemoveExisting4", "Mod","TEST FOR EXISTING COMMAND STUFF");
INSERT INTO commands(command, role, response) VALUES("!testRemoveExisting5", "Mod","TEST FOR EXISTING COMMAND STUFF");

/*
  Permit Table - stores the permited users and the expiration time of the permit
  Timestamp is in format 'YYYY-MM-DD HH:MM:SS'
*/
CREATE TABLE permits(
  id INT AUTO_INCREMENT NOT NULL,
  user VARCHAR(32) UNIQUE NOT NULL,
  expiration TIMESTAMP NULL,
  PRIMARY KEY(id)
);

/*TODO insert some existing permits to test with*/
