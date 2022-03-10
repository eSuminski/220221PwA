-- postgres allows the use of constraints which help determine the rules for what you can and,
-- sometimes more important to know, what you can't do with your tables.

-- primary key: if a column is labeled as a primary key, which is done after declaring the type,
-- then that column is considered to have the unique and not null constraints on it. This means that 
-- there must be a non-null value, and it must be unique in the table

-- foreign key: a column labeled as a foreign key is supposed to reference a primary key on another table

create table customers(
	customer_id serial primary key,
	first_name varchar(20),
	last_name varchar(20)
);


create table accounts(
	account_id serial primary key,
	customer_id int,
	balance dec(15,2),
	constraint accounts_foreign_key foreign key(customer_id) references customers(customer_id) on delete cascade
);

insert into customers values(default, 'Eric', 'Suminski');
insert into accounts values(default, 1, 10000); -- this will not work if I don't provide an existing customer id
delete from customers where customer_id = 1; -- this will remove not only my customer id, but any account records associated with it

-- unique: it is possible to set a unique constraint, which simply means the record must have a unique value (null is accepted)

-- not null: this simply means there must be a value in the column, even if it is a duplicate

-- check: check makes sure that the record meets some criteria

create table accounts(
	account_id serial,
	customer_id int,
	balance dec(15,2) check(balance > 0)
);

insert into accounts values(default, 1, -100);-- this will not work because -100 is less than 0