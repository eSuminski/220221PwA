package com.revature.api;

import com.revature.dal.PersonDAOImp;
import com.revature.dal.PersonDAOInterface;
import com.revature.sl.PersonServiceImp;
import com.revature.sl.PersonServiceInterface;
import io.javalin.Javalin;

public class App {

    public static void main(String[] args) {
        Javalin app = Javalin.create(config ->{
            config.enableCorsForAllOrigins();
            config.enableDevLogging();
        });

        // this is coding to the interface: set the type as the interface, the object constructor used is form the implementation class
        PersonDAOInterface personDao = new PersonDAOImp();
        PersonServiceInterface personService = new PersonServiceImp(personDao);
        PersonController personController = new PersonController(personService);


        app.get("/", personController.sayHello);

        app.post("/person", personController.createPerson);

        app.get("/person/{id}", personController.getPerson);



        app.start();



    }// main end

}
