create table players(
	player_id serial primary key,
	first_name varchar(20),
	last_name varchar(20)
);

-- needed for select player test
insert into players values(-1,'Billy','Bob');
-- needed for update player test, need to update after tests
insert into players values(-2,'needs','names');
update players set first_name = 'needs', last_name ='names' where player_id = -2;

-- needed for delete player test
insert into players values(-3,'delete','me');
