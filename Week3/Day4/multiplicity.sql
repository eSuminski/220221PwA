-- Multiplicity is a way of describing the relationship between tables that share a primary/foreign key relationship

-- 1:1

create table humans(
	human_id serial primary key
);

create table brains( -- 1:1 relationship with humans
	brain_id serial primary key,
	human_id int unique,
	constraint brain_fk foreign key(human_id) references humans(human_id) on delete cascade
);

create table hands( -- 1:many relationship with humans
	hand_id serial primary key,
	human_id int,
	digits int,
	constraint hands_fk foreign key(human_id) references humans(human_id) on delete cascade
);

-- 1:many

create table customers(
	customer_id serial primary key,
);

create table accounts(
	account_id serial primary key,
	customer_id int, -- there is no unique constraint here, so these tables have a 1:many relationship
	balance dec(15,2),
	constraint account_foreign_key foreign key (customer_id) references customers(customer_id) on delete cascade
);

-- many:many

create table teachers(
	teacher_id serial primary key
);

create table students(
	student_id serial primary key
);

create table teachers_students_join_table(
	join_id serial primary key,
	teacher_id int,
	student_id int,
	constraint teacher_fk foreign key(teacher_id) references teachers(teacher_id) on delete cascade,
	constraint student_fk foreign key (student_id) references students(student_id) on delete cascade
);

select student_id from teachers_students_join_table where teacher_id  = 1; -- this gives me all student ids associated with teacher 1