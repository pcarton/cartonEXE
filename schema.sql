DROP TABLE IF EXISTS commands;


/*
  Command Table - stores the static command responses
*/
CREATE TABLE commands(
  id INT AUTO_INCREMENT NOT NULL,
  command VARCHAR(80) NOT NULL,
  role VARCHAR(10) NOT NULL,
  response VARCHAR(80) NOT NULL,
  PRIMARY KEY(id)
);
