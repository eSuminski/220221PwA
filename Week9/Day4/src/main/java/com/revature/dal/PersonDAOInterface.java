package com.revature.dal;

import com.revature.entity.Person;

public interface PersonDAOInterface {

    Person createPerson(Person person);

    Person getPerson(int id);

}
