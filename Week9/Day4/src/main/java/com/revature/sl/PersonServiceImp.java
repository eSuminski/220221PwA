package com.revature.sl;

import com.revature.custom_exception.NoDerrek;
import com.revature.custom_exception.PersonNotFound;
import com.revature.dal.PersonDAOInterface;
import com.revature.entity.Person;

public class PersonServiceImp implements PersonServiceInterface{
    public PersonDAOInterface personDAO;

    public PersonServiceImp(PersonDAOInterface personDAO) {
        this.personDAO = personDAO;
    }

    @Override
    public Person serviceCreatePerson(Person person) {
        if(person.getName().equals("Derrek")){
            throw new NoDerrek("No Derreks allowed!");
        } else {
            return personDAO.createPerson(person);
        }
    }

    @Override
    public Person serviceGetPerson(int id) {
        Person person = personDAO.getPerson(id);
        if(person == null){
            throw new PersonNotFound("Could not find the person");
        } else {
            return person;
        }
    }
}
