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

INSERT INTO commands(command, role, response) VALUES("!testRemoveExisting1", "Caster","TEST FOR EXISTING COMMAND STUFF");
INSERT INTO commands(command, role, response) VALUES("!testRemoveExisting2", "Mod","TEST FOR EXISTING COMMAND STUFF");
INSERT INTO commands(command, role, response) VALUES("!testRemoveExisting3", "Sub","TEST FOR EXISTING COMMAND STUFF");
INSERT INTO commands(command, role, response) VALUES("!testRemoveExisting4", "Follower","TEST FOR EXISTING COMMAND STUFF");
INSERT INTO commands(command, role, response) VALUES("!testRemoveExisting5", "Normal","TEST FOR EXISTING COMMAND STUFF");

INSERT INTO commands(command, role, response) VALUES("!testExisting1", "Caster","TEST FOR EXISTING COMMAND STUFF ONE");
INSERT INTO commands(command, role, response) VALUES("!testExisting2", "Mod","TEST FOR EXISTING COMMAND STUFF TWO");
INSERT INTO commands(command, role, response) VALUES("!testExisting3", "Sub","TEST FOR EXISTING COMMAND STUFF THREE");
INSERT INTO commands(command, role, response) VALUES("!testExisting4", "Follower","TEST FOR EXISTING COMMAND STUFF FOUR");
INSERT INTO commands(command, role, response) VALUES("!testExisting5", "Normal","TEST FOR EXISTING COMMAND STUFF FIVE");

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

INSERT INTO permits(user,expiration) VALUES("TestUser1","2009-06-11 08:55:36");
INSERT INTO permits(user,expiration) VALUES("TestUser3","2009-06-11 08:55:36");
INSERT INTO permits(user,expiration) VALUES("TestUser4","2009-06-11 08:55:36");
INSERT INTO permits(user,expiration) VALUES("TestUser5","2009-06-11 08:55:36");
INSERT INTO permits(user,expiration) VALUES("TestUser6","2009-06-11 08:55:36");
INSERT INTO permits(user,expiration) VALUES("TestUser7","2009-06-11 08:55:36");
INSERT INTO permits(user,expiration) VALUES("TestUser8","2009-06-11 08:55:36");
