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

#### käyttäjä-tiimi -liitostaulu:
```
CREATE TABLE user_team (
	user_id INTEGER, 
	team_id INTEGER, 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	FOREIGN KEY(team_id) REFERENCES team (id)
);  
```
## SQL-kyselyt

#### käyttäjän lisääminen (normaalikäyttäjä):
```
INSERT INTO Account (username, password, role_id) VALUES (?, ?, 2);
```
#### joukkueen lisääminen, liittäminen käyttäjään ja lisäys edustettavaksi joukkueeksi:
```
INSERT INTO Team (name) VALUES (?);
INSERT INTO user_team (user_id, team_id) VALUES (?, ?);
UPDATE Account SET representive_team_id = ?;
``` 
#### joukkueen poistaminen käyttäjän joukkueista:
```
DELETE FROM user_team WHERE user_id = ? AND team_id = ?
```
#### tietovisakysymyksen lisäys, muokkaus ja poisto
```
INSERT INTO Question (question, answer, answered_correctly, category, quiz_date)  
VALUES (?, ?, ?, ?, ?);
UPDATE Question SET (?) VALUES (?);
DELETE FROM Question WHERE question.id = ?;
```
#### kysymysten listaus joukkueen mukaan, aikajärjestyksessä
```
SELECT * FROM Question WHERE team_id = ? ORDER BY quiz_date DESC;
```
#### joukkueelle vaikein kysymyskategoria, ja kuinka monta prosenttia ko. kategorian kysymyksistä on oikein:
```
SELECT MIN(avg_answered_correctly) AS average, category  
FROM (SELECT AVG(question.answered_correctly) AS avg_answered_correctly, category  
FROM Question WHERE team_id = ? GROUP BY category) AS avg_answers;
```
#### menestynein joukkue (eniten oikeita vastauksia prosentuaalisesti):
```
SELECT name, AVG(answered_correctly) AS avg FROM Team  
JOIN Question ON question.team_id = team.id  
GROUP BY team.name ORDER BY avg DESC limit 1;
```
