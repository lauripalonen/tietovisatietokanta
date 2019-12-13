# SQL-kyselyt

## CREATE TABLE -lauseet

#### Roolitaulu: (erottelee ADMIN- ja normaalikäyttäjän toiminallisuuksia):
```
CREATE TABLE role (
	id INTEGER NOT NULL, 
	role VARCHAR(8) NOT NULL, 
	PRIMARY KEY (id)
);  
```

#### Tiimitaulu:  
```
CREATE TABLE team (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);  
```
#### Kysymystaulu:  
```
CREATE TABLE question (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	question VARCHAR(144) NOT NULL, 
	answer VARCHAR(144) NOT NULL, 
	category VARCHAR(144), 
	answered_correctly BOOLEAN, 
	quiz_date DATE, 
	team_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (answered_correctly IN (0, 1)), 
	FOREIGN KEY(team_id) REFERENCES team (id)
);  
```
#### Käyttäjätaulu:
```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	representive_team_id INTEGER, 
	role_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);  
```

#### käyttäjä-tiimi -liitostaulu:
```
CREATE TABLE user_team (
	user_id INTEGER, 
	team_id INTEGER, 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	FOREIGN KEY(team_id) REFERENCES team (id)
);  
```
