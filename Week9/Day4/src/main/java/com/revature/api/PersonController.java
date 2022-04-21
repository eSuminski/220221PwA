package com.revature.api;

import com.google.gson.Gson;
import com.revature.custom_exception.NoDerrek;
import com.revature.custom_exception.PersonNotFound;
import com.revature.entity.Person;
import com.revature.sl.PersonServiceInterface;
import io.javalin.http.Handler;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class PersonController {

    /*
        Note: I only have the logger here in the example, but you could create a logger in each level of your
        application to be more specific with your log notes. The key is to log pertinent information: how you do
        that is up to you and your team
     */
    public static Logger logger = LogManager.getLogger(PersonController.class);

    // notice I only declare the service interface, not the dao interface. that will be handled in the App class
    public PersonServiceInterface personService;

    public PersonController(PersonServiceInterface personService) {
        this.personService = personService;
    }

    public Handler sayHello = ctx -> {
        logger.info("creating hello message");
        ctx.result("Hello!");
        logger.info("hello message created");
    };

    public Handler createPerson = ctx -> {
        try{
            logger.info("starting process to create a person");
            Gson gson = new Gson();
            logger.info("getting http request body");
            String body = ctx.body();
            logger.info("creating Person object from http request body");
            Person person =gson.fromJson(body, Person.class);
            logger.info("attempting to add person to database");
            Person result = personService.serviceCreatePerson(person);
            logger.info("successfully added person with info: " + result + " to database");
            String resultJson = gson.toJson(result);
            ctx.result(resultJson);
            ctx.status(201);
            logger.info("all done!");
        } catch(NoDerrek e){
            logger.warn("DERREK ATTEMPTED TO GET IN THE DATABASE! THIS IS A TRAVESTY");
            ctx.result(e.getMessage());
            ctx.status(405);
        }
    };

    public Handler getPerson = ctx -> {
        try{
            logger.info("starting process of getting a person from the database");
            logger.info("getting the person id from the path parameter");
            int id = Integer.parseInt(ctx.pathParam("id"));
            logger.info("attempting to retrieve person based on the given id");
            Person person = personService.serviceGetPerson(id);
            Gson gson = new Gson();
            logger.info("converting Person object to JSON");
            String personJson = gson.toJson(person);
            ctx.result(personJson);
            ctx.status(200);
            logger.info("all done!");
        } catch (PersonNotFound e){
            logger.warn(e.getMessage());
            ctx.result(e.getMessage());
            ctx.status(404);
        }
    };

}
