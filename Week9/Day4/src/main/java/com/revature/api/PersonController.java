package com.revature.api;

import com.google.gson.Gson;
import com.revature.custom_exception.NoDerrek;
import com.revature.custom_exception.PersonNotFound;
import com.revature.entity.Person;
import com.revature.sl.PersonServiceInterface;
import io.javalin.http.Handler;

public class PersonController {
    public PersonServiceInterface personService;

    public PersonController(PersonServiceInterface personService) {
        this.personService = personService;
    }

    public Handler sayHello = ctx -> {
        ctx.result("Hello!");
    };

    public Handler createPerson = ctx -> {
        try{
            Gson gson = new Gson();
            String body = ctx.body();
            Person person =gson.fromJson(body, Person.class);
            Person result = personService.serviceCreatePerson(person);
            String resultJson = gson.toJson(result);
            ctx.result(resultJson);
            ctx.status(201);
        } catch(NoDerrek e){
            ctx.result(e.getMessage());
            ctx.status(405);
        }
    };

    public Handler getPerson = ctx -> {
        try{
            int id = Integer.parseInt(ctx.pathParam("id"));
            Person person = personService.serviceGetPerson(id);
            Gson gson = new Gson();
            String personJson = gson.toJson(person);
            ctx.result(personJson);
            ctx.status(200);
        } catch (PersonNotFound e){
            ctx.result(e.getMessage());
            ctx.status(404);
        }
    };

}
