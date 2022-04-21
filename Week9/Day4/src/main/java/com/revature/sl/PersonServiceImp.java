package com.revature.sl;

import com.revature.custom_exception.NoDerrek;
import com.revature.custom_exception.PersonNotFound;
import com.revature.dal.PersonDAOInterface;
import com.revature.entity.Person;

public class PersonServiceImp implements PersonServiceInterface{
    /*
        Notice I create a field in this class for a personDAO object. I need this in order to transfer
        information from this service layer object into the data access layer
     */
    public PersonDAOInterface personDAO;

    /*
        make sure you create a constructor that initializes the value of the field when you create a service
        object
     */
    public PersonServiceImp(PersonDAOInterface personDAO) {
        this.personDAO = personDAO;
    }

    /*
        remember: your service layer only handles business logic: any interaction with the database is handled
        by your data access layer.
     */
    @Override
    public Person serviceCreatePerson(Person person) {
        if(person.getName().equals("Derrek")){
            throw new NoDerrek("No Derreks allowed!");
        } else {
            // once the business logic has been handled the data is passed to the data access layer
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
