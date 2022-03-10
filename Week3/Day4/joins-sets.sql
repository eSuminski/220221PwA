-- Postgres allows you to combine data from different tables in unique ways. You can use joins
-- to place data from tables next to one another, or you can use set operations to combine like
-- data between multiple tables

-- you can use the inner join to link data between tables via a specified value
select * from players inner join teams on players.team_id = teams.team_id ;

-- you can also use a left, right, and full outer join to group your tables 

-- this will get all the records from the players table, and any entries that don't have a match 
-- on the teams table will fill in the team table columns with null
select * from players left join teams on players.team_id = teams.team_id ;

-- this will get all the records from the teams table, and any entries that don't have a match 
-- on the players table will fill the players table columns with null
select * from players right join teams on players.team_id = teams.team_id ;

-- a full outer join returns all the records of the two tables, with null values provided
-- when there is no match between the tables
select * from players full outer join teams on players.team_id  = teams.team_id ;

-- a cross join shows you all possible combinations of data, I think it is neat
select* from players cross join teams;

-- if join operations place tables next to one another, you can think of set operations placing 
-- columns on top of one another. You can perform these operations on columns with the same
-- data type

select team_id from players union select team_id from teams;

select team_id from players intersect select team_id from teams;