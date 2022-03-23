-- Normalization is simply a way of organizing your data through a set of constraining principles
-- The higher levels of normalization have more constraining principles to follow

-- First normal form requires at least one primary key and it requires atomic columns

CREATE TABLE person(
	-- notice there is no primary key for this table: it is not a normalized table
	first_name varchar(20),
	last_name varchar(20),
	full_name varchar(50) -- this COLUMN IS NOT considered ATOMIC, it can be broken down further
);

INSERT INTO person VALUES('Eric', 'Suminski', 'Eric Suminski'); -- we can see here that the FULL name COLUMN IS a combination OF the FIRST AND SECOND COLUMN

-- the table below has at least one primary key (in this case a composite key) and all columns are atomic.
-- this table is following first normal form constraints
CREATE TABLE player(
	player_id serial PRIMARY KEY,
	first_name varchar(20),
	last_name varchar(20),
	shots_attempted int,
	shots_made int,
	shooting_percentage float,
	team_id int PRIMARY KEY,
	team_name varchar(50)
);

-- second normal form requires that you follow first normal form constraints, but also that you have no
-- partial dependencies

CREATE TABLE player(
	player_id serial PRIMARY KEY, --since there IS ONLY one PRIMARY KEY, AND ALL columns ARE associated WITH it, we have SECOND normal form
	first_name varchar(20),
	last_name varchar(20),
	shots_attempted int,
	shots_made int,
	shooting_percentage float
);

-- Third normal form requires you follow the second normal form constraints, but also remove transitive properties
-- a transitive property is something that can be determined via a combination of other columns

CREATE TABLE player(
	player_id serial PRIMARY KEY,
	first_name varchar(20),
	last_name varchar(20),
	shots_attempted int,
	shots_made int
	-- we removed the shooting percentage column, so there are no longer any transitive properties
	-- this table is now follows third normal form constraints
);
