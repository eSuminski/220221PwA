package com.revature.dal;

import com.revature.entity.Person;

import java.util.ArrayList;
import java.util.List;

public class PersonDAOImp implements PersonDAOInterface{
    // your database handles this part, this is here for simplicity
    public static List<Person> people = new ArrayList<>();
    public static int idGenerator = 1;


    @Override
    public Person createPerson(Person person) {
        person.setId(idGenerator);
        idGenerator++;
        people.add(person);
        return person;
    }

    @Override
    public Person getPerson(int id) {
        for(Person p : people){
            if(p.getId() == id){
                return p;
            }
        }
        return null;
    }
}
