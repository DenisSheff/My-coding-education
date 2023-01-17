
-- create
CREATE TABLE GROUPMATE (
  mateId INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  adress TEXT NOT NULL
);

-- insert
INSERT INTO GROUPMATE (name, age, adress) VALUES ( 'Alevtina', 34, 'Klin');
INSERT INTO GROUPMATE (name, age, adress) VALUES ( 'Andrew', 23, 'Moscow');
INSERT INTO GROUPMATE (name, age, adress) VALUES ( 'Lubov', 33, 'Moscow');
INSERT INTO GROUPMATE (name, age, adress) VALUES ( 'John', 43, 'Bolshakovo');
INSERT INTO GROUPMATE (name, age, adress) VALUES ( 'Dimitrii', 20, 'Zeya');
INSERT INTO GROUPMATE (name, age, adress) VALUES ( 'Svyatopolk', 53, 'Vladivostok');
INSERT INTO GROUPMATE (name, age, adress) VALUES ( 'Dasha', 27, 'Khabarovsk');
INSERT INTO GROUPMATE (name, age, adress) VALUES ( 'Yura', 49, 'Blagoveshchensk');
INSERT INTO GROUPMATE (name, age, adress) VALUES ( 'Vika', 18, 'Moscow');
INSERT INTO GROUPMATE (name, age, adress) VALUES ( 'Nikita', 24, 'Moscow');
 
-- fetch 
SELECT * FROM GROUPMATE WHERE adress = 'Moscow' and age < 30 and age >= 18;

