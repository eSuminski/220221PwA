## AWS RDS
Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

AWS RDS automates many tasks:
- managing backups
- software patching
- auto failure detection
- recovery

AWS RDS offers different database types with varying combinations of CPU, memory, storage, and networking capacity . This gives you the flexibility to choose the appropriate mix of resources for your database.

AWS RDS offers multiple types of databases (Oracle, Postgre, etc) which are free to try. The model is "pay as you go"

RDS databases are useful when you need your data to be related (rows and columns) and when you need to link data between tables

Amazon offers different regions that house cloud computing resources, when you set up your AWS RDS you want to select a region close to your location. However, to make your instance fault tolerant, you will want to deploy multiple instances in multiple zones (zones are areas within a region)

There are multiple ways to interact with an AWS RDS:
- AWS Management Console
- AWS CLI
- AWS SDK (programatically)

AWS RDS is a managed service, so you have limited control over your database. Another option is yo use an EC2 and install a database on it. This gives you more control, but you lose the automatic management of your database.
## SQL 
Structured Query Language is tool for interacting with an SQL database. It allows you to create tables, manipulate them, create user rolls, and create some functionality in the database. Relational Databases are orginized in schemas
## Schemas
These are data structures that hold different tables within the database. They are used for organization, and are enforced by using constraints (see constraints section for more details)
## Sub Languages
These are the five sublanguages off SQL, and some of their key words
### DDL
```sql
--these are the commands that let us set up and alter tables within our database

--create allows us to make new tables. We define the columns and their types inside parenthesis
create table simple_table(
	first_name varchar(50),
	last_name varchar(50)
);

--alter lets us make changes to tables and their columns
alter table simple_table add column person_id serial;

--truncate will remove all the data within a table without deleting the table itself, as long as their are no constraint issues
truncate table simple_table;

--drop will delete a table and its data, as long as their are no constraint issues
drop table simple_table;

--these commands are not reversable: there is no option to do a rollback
```
### DML
```sql
--these are the CRUD operators (Create, Read, Update, Delete)

--insert is used to add data into a table
insert into names values(default, 'Eric', 'Suminski');

--update is used to change data in a table
update names set first_name = 'Sam' where person_id = 1;

--select is used to get data from a table. This is sometimes categorized under DQL
select * from names where person_id = 1;

--delete is used to remove data from a table
delete from names where person_id = 1;
```
### DCL
```sql
--these commands manage users and privliges on the database

--this creates a basic user with the name test with password test. Useful for allowing limited access
CREATE ROLE test NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT LOGIN PASSWORD 'test';

--this allows anyone who logs in as test to perform all actions on the given table
GRANT ALL ON TABLE practice.names TO test;

--this removes all rights to perform actions on the table from test user
REVOKE ALL ON TABLE practice.names FROM test;
```
### TCL
```sql
--these commands can start, end, and rollback transactions. Use them if you want fine control over your queries

--this starts a new transaction
begin;
	insert into names values(default, 'Eric', 'Suminski');
    --this creates a spot we can rollback to if needed
	savepoint my_savepoint;
	insert into names values(default, 'Sam', 'Suminski');
    --this will rollback the transaction to the save point, so we lose the Sherri info
	rollback to savepoint my_savepoint;
    --this removes the savepoint, good pratice
	release savepoint my_savepoint;
--this will commit the transaction, can also use end
commit; -- or end
```
## Constraints
Constraints are used to limit or identify data within your tables. You should know these:
- PRIMARY KEY: makes the column an identifier. Combination of unique and not null
    - multiple primary keys are called composite keys
    - columns that could work as primary keys are called candidate keys
- FOREIGN KEY: makes the column reference a primary key on another table
- NOT NULL: column must have a value
- UNIQUE: column value must be different from all others in table
- CHECK: use when you need to ensure a condition is met (number > 0, for instance)
```sql
create table names(
    -- this is now required to be not null and unique
	person_id serial primary key,
	first_name varchar(10),
	last_name varchar(10)
);

create table foreign_key_example(
	foreign_key_example_id serial,
	foreign_key int,
    --this makes it so our foreign_key column references the person_id column. Any entries to this table MUST reference someone on the names table
	constraint my_foreign_key foreign key(foreign_key) references names(person_id)
);
```
## Functions
There are two kinds of functions in SQL: aggregate and scalar. Aggregate functions work on groups of data, whereas scalar functions work on single pieces of data.

Some common Aggregate functions:
```sql
-- sum(): returns the sum of values in a group of data
select sum(person_id) from names;
-- min(): returns the smallest value in group of data
select min(person_id) from names;
-- max(): returns the largest value in a group of data
select max(person_id) from names;
-- count(): returns the number of rows of data in the group
select count(person_id) from names;
-- avg(): returns the average in a group of data
select avg(person_id) from names;
```

Some common scalar functions:
```sql
--now(): returns the current date and time
select now();
--upper(): returns the string value in all uppercase
select upper(first_name) from names where person_id = 1; 
--lower(): returns the string value in all lowercase
select lower(first_name) from names where person_id = 1;
--length(): returns the length of the value
select length(first_name) from names where person_id = 1;
--round(): takes two arguments, the first is the value to round, the second optional one is the acceptable number of decimal places
select round(person_id, 2) from names where first_name = 'Eric';
```
## Referential Integrity
This is the idea that we should have no orphaned records. If an entry has a foreign key, it NEEDS to reference an existing record. If the primary record is deleted then the foreign record needs to have a response. This response could be to self delete, or even to stop the parent record from being deleted. You have a few common options:
- on delete cascade: deletes the data that has a foreign relationship to the primary data
- on delete restrict: prevents the primary data from being deleted
- on delete update: allow the foreign key to update, but if it breaks referential integrity the whole transaction will fail
## Multiplicity
This describes the relationship between tables. There are three ways tables can relate:
- one-to-one: only one entity in a table references another
```sql
create table person(
	person_id serial primary key
);

create table brain(
	brain_id serial primary key,
	person_id int unique, --notice the unique constraint: only one brain can be attached to a person
	constraint brain_fk foreign key (person_id) references person(person_id)
);
```
- one-to-many (or many-to-one): many entities in a table can reference one other entity in the other table
```sql
create table team(
	team_id serial primary key
);

create table player(
	player_id serial primary key,
	team_id int, --many players can have the same team id, since they play on the same team
	constraint player_fk foreign key(team_id) references team(team_id)
);
```
- many-to-many: many entities in a table can reference many other entities in another table. Because a direct link can not be established between the two (think teachers and students: many teachers can have many students, and many students can have many teachers) you need to create a junction table (sometimes called a join table).
```sql
create table teacher(
	teacher_id serial primary key
);

create table student(
	student_id serial primary key
);
--notice there are no foreign keys in the student or teacher tables: their relationship is handled by the join table classroom
create table classroom(
	classroom_id serial primary key,
	teacher_id int,
	student_id int,
	constraint teacher_fk foreign key(teacher_id) references teacher(teacher_id),
	constraint student_fk foreign key(student_id) references student(student_id)
);
```
## Normalization
There are three levels of normalization to be familiar with:
```sql
--there is no normalization happening here
create table not_1nf(
	first_and_last_name varchar(50),
);
--there is a primary key, and all columns are atomic. This is 1NF
create table first_nf(
	person_id serial primary key,
	job varchar(50) primary key,
	first_name varchar(50),
	last_name varchar(50),
	job_title varchar(50)
);
--this is 1NF plus it removed the composite key, so all columns reference a single primary key. This is 2NF
create table second_nf(
	person_id serial primary key,
	first_name varchar(50),
	last_name varchar(50)
);
--this is 2NF, but the total cost column is unneccessary, since we could get it from items purchased and item price. It is transitive
create table not_third_nf(
	order_id serial primary key,
	item varchar(50),
	items_purchased int,
	item_price decimal,
	total_cost decimal
);
--this is 3NF: it conforms to 2NF and it has no transitive properties
create table third_nf(
	order_id serial primary key,
	item varchar(50),
	items_purchased int,
	item_price decimal
);
```
## ACID
Any DML actions before a commit are called  transactions. Every transaction should have the ACID properties

Atomicity
- all transactions must succeed for a commit to happen. If any fail, there is no commit

Consistency
- all transactions must enforce existing constraints

Isolation
- multiple concurent transactions should not interfere with one another

Durability
- committed transactions should be persisted, even if there is some catastrophic failure (power outage, system, crash, etc). 
## Read Phenomena
These three read phenomena are problematic: isolation levels are used to deal with them:
- Dirty Read: reading data that is uncommitted
- Non-repeatable read: when a row is read twice in a transaction and the values are different
- Phantom Read: reading data that is being added or modified by a running transaction
## Isolation Levls
These help prevent the various read phenomena
- Read Uncommited
	- This is bad, don't do this
	- dirty reads are common at this level
	- data is inconsistently: you don't know if you are reading committed data or not
- Read Committed
	- default for Postgre and Oracle
	- Only committed data can be seen by other transactions
	- Prevents dirty reads, but not phantom reads
	- locks the row in the transaction from being selected by other transactions
- Repeatable Read
	- not common
	- read and write locks
	- still allows phantom reads, but not non-repreatable reads
- Serializable
	- locks read, write, and range (essentially locks down the data part of the transaction)
	- prevents phantom reads
	- tables being read cannot be interacted with until the transactions are committed
## Joins
Joins allow you to combine table data by putting their columns next to each other to view
inner
```sql
create table team(
	team_id serial primary key,
	team_name varchar(50)
);

create table player(
	player_id serial primary key,
	team_id int,
	player_name varchar(50),
	constraint team_fk foreign key(team_id) references team(team_id)
);
-- this will return the data ordered by what team the player is on. It will match the player to their team, and contains all data
select * from player inner join team on team.team_id = player.team_id order by player.team_id ;

```
the outter joins are left, full outer, and right join
```sql
-- this left join returns all data in the team (left) table and any matching records in the player table
select * from team left join player on team.team_id = player.team_id ;

-- this right join returns all the data in the player(right) table and any matching records in the team table
select * from team right join player on team.team_id = player.team_id ;

-- this full outer join returns all data in both the team and player tables
select * from team full outer join player on team.team_id = player.team_id ;

```
think of the cross join as showing possibility (cartesian product)
```sql
--all players will be matched with all teams
select * from team cross join player ;
```
## Set Operations
sets allow you to stack tables on top of each other. Requires columns with the same names 

unions combine like columns and return one table that is a combined product
```sql
-- returns all id values without any duplicates (make union all to allow duplicates)
select team.team_id from team union select player.team_id from player;
```
intersect only groups the elements that are common to the two tables
```sql
-- this will only return those team_ids that have a player assigned to them
select team_id from team intersect select team_id from player;
```
## Data Types
There are many different datatypes you can use: make sure you know the different categories and are familiar with at least a few of their specific types: int and varchar will be your bread and butter for the most part in this course
## Stored Procedures and Functions
You can make your own functions in SQL, and you can also make Stored Procedures. They have slight differences from one another
```sql
create or replace function addition( num1 int, num2 int) returns int as $$
	-- any local variables need to be defined at the top of the function
	declare
		total int;
	-- actual logic of the function goes between a begin and end statement
	begin
		total = num1 + num2;
		-- make sure to return a value
		return total;
	end
-- you have to declare the language you use to make the function
$$ LANGUAGE plpgsql;

-- this line adds the two inputs together and returns the result. Must be ints or there is an error
select addition(5,5);
```
stored procedures are accessed by using the call keyword. 
```sql
create table accounts (
    id int generated by default as identity,
    name varchar(100) not null,
    balance dec(15,2) not null,
    primary key(id)
);

insert into accounts(name,balance)
values('Bob',10000);

insert into accounts(name,balance)
values('Alice',10000);

create or replace procedure transfer(
   sender int,
   receiver int, 
   amount dec
)
language plpgsql    
as $$
begin
    -- subtracting the amount from the sender's account 
    update accounts 
    set balance = balance - amount 
    where id = sender;

    -- adding the amount to the receiver's account
    update accounts 
    set balance = balance + amount 
    where id = receiver;

    commit;
end;$$

call transfer(1,2,1000);-- this will call the stored procedure and transfer funds between accounts
```