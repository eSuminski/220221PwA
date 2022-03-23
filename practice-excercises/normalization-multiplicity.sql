-- this script contains some practice exercises for getting familiar with normalization and multiplicity

-- the three tables below are not normalized: below them are three sections labeled 1NF, 2NF, and 3NF.
-- your exercise is to remake each table into a normalized version for each of the three levels

CREATE TABLE employees(
	employee_id int,
	job_id int,
	first_and_last_name varchar(100),
	job_title varchar(20)
);

CREATE TABLE players(
	player_id int,
	player_first_and_last_name varchar(100),
	team_id int,
	team_name varchar(20),
	shots_attempted int,
	shots_made int,
	shooting_percentage float
);

CREATE TABLE dogs(
	dog_id int,
	owner_id int,
	breed varchar(50),
	pet_name varchar(50)
	owner_name varchar(50)
);

-- 1NF

-- 2NF

-- 3NF

-- create two tables in the space below, one called humans and the other called stomachs, that have a 1:1 relationship with each other
-- (one human can have one stomach)

CREATE TABLE humans();

CREATE TABLE stomachs();

-- create two tables below, one called customers and the other called purchases, where customers has a 1:many relationship with purchases
-- (one customer can have many purchases)

CREATE TABLE customers();

CREATE TABLE purchases();

-- create three tables below, one called teachers, one called classrooms, and the last called teacher_classroom_join.
-- use the join table to create a many:many relationship between the teachers and classrooms tables
-- (many teachers can have many classrooms)

CREATE TABLE teachers();

CREATE TABLE classrooms();

CREATE TABLE teacher_classroom_join();

