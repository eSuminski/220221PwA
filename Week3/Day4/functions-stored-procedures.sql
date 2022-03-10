-- there are some common aggregate functions in postgres that you can use to perform some operation
-- on a group of data 

-- this adds the values of all the person_ids and returns their sum
select sum(person_id) from persons;

-- min can be used to get the minimum value
select min(person_id) from persons;

-- max can be used to get the maximum value 
select max(person_id) from persons;

-- count can be used to get the number of rows that have the selected value 
select count(person_id) from persons;

-- avg can be used to get the average value of a group of data 
select avg(person_id) from persons;

-- scalar functions are used to affect individual pieces of data in your database

-- now is useful to get the current date and time
select now();
 -- this will return all the first names in the table upper case
select upper(first_name) from persons;

-- this will return the first name of the person with id 1 in all lowercase
select lower(first_name) from persons where person_id = 1;

-- this will return the length of the string
select length(first_name) from persons where person_id = 1;

-- you have the ability to create your own custom functions. 
-- the dollar signs book end the content of our custom function
create or replace function addition(num int, num2 int) returns int as $$
	-- we first need to declare any local variables, in this case, just the total we will return
	declare 
		total int; -- type should match returns type
	begin 
	-- in here we write out the logic of our custom function, making use of the arguments and local variable we created
		total = num + num2; 
		return total; -- make sure to actually return the value you want
	end
$$ language plpgsql; -- make sure to note the language you are using, in our case, procdedural language PostgreSQL

select addition(5,5);

-- stored procedures are similar to functions in that they perform an operation upon your data,
-- but they are more robust than a simple function

create table accounts(
	account_id serial,
	owner_name varchar(20),
	balance dec(15,2)
);

insert into accounts values(default, 'Billy', 10000);
insert into accounts values(default, 'Sally', 10000);

create or replace procedure transfer(
	sender int,
	reciever int,
	ammount dec
)
language plpgsql
as $$
begin 
	-- first I need to remove the transfer value from the sender balance 
	update accounts set balance = balance - ammount where account_id = sender;
	-- second, I need to add the transfer value to the reciever balance
	update accounts set balance = balance + ammount where account_id = reciever;
	commit;
end;
$$

call transfer(1,2,1000);

