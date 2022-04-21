package com.revature.sl;

import com.revature.entity.Person;

public interface PersonServiceInterface {

    Person serviceCreatePerson(Person person);

    Person serviceGetPerson(int id);

}
