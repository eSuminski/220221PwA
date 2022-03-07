-- We are using Amazon Web Services to host our Postgres Database. These database are a very
-- popular option for creating "relational" databases. 

-- to interact with our database we will be using Structured Query Language. SQL is a modern
-- syntax for interacting with databases, and in particular, we will be using PostgreSQL to 
-- handle interacting with our database

-- schemas are data structures inside of your database that hold your tables. Your tables are 
-- the data structures that will contain the information and/or data specific to your needs. 

-- tables consists of columns and rows. The columns represent the data you are keeping track of 
-- (think usernames, passwords, unique ids, etc) and the rows represent the actual inputs of data 
-- (user's ACTUAL username, ACTUAL password, etc)

-- whenever you want to create, update, or delete a table, you use the Data Definition Sub languge
-- of SQL (DDL)


--  this is the simplest way of creating a table: use the key words create and table, give it a name,
-- and then list the column names and data types
create table people(
	first_name varchar(20),
	last_name varchar(20)
);

-- you can use the alter key word to make changes to an existing database
alter table people add column personal_id serial;

-- if you need to get rid of your tables you can use the drop keyword
-- you can also say drop table if exists to avoid possible sql errors
drop table if exists people;

-- if you want to clear the contents of a table you use the trunate key word 
truncate table people;


-- once you have a a table in your database you need to put information inside of it To do this,
-- you need to use your Data Manipulation Language (DML)

-- this is how you create data inside of your table: us the insert key word
insert into people values('Eric', 'Suminski', default);
insert into people values('Sam', 'Suminski', default);
insert into people values('Evil', 'Bob',default);

-- this is how you delete one or more entries from your table
delete from people where personal_id = 2;
delete from people where first_name = 'Eric'; -- this will find all entries with the first name Eric and delete them

-- this is how you update entries in your tables
update people set first_name = 'Eric' where first_name = 'Sam';

-- to get information from our tables we use the select key word
-- some call this operation part of the Data Query Sublanguage (DQL) 
select first_name from people where personal_id = 12;
select first_name, last_name from people where personal_id = 12;
select first_name, last_name, personal_id from people where personal_id =12;
select * from people where personal_id = 12; -- this is a shorthand to get all column information

select * from people; -- this gives me every record inside the table
select * from people where last_name = 'Suminski';

-- another sub language you should be aware of is the Transaction Control Sublanguage 
-- using transaction control, we can roll back any changes we don't want before commiting our queries
begin;
	insert into people values ('Good', 'Sally', default);
	savepoint Sallys_save_point;
	insert into people values ('neutral', 'Pete', default);
	rollback to Sallys_save_point;
	release savepoint Sallys_save_point;
commit;
end; -- use the end command if your transaction block fails: this is needed because a failed transaction block is considered open until the end or commit command is actually run

-- Data Control Language handles user privileges: essentially, you use DCL to determine who can do what in your database
create role simple_user;
-- if I want to give permission to access a schema:
grant usage on schema public to simple_user;
grant select on table public.people to simple_user;