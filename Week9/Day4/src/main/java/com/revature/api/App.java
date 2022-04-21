package com.revature.api;

import com.revature.dal.PersonDAOImp;
import com.revature.dal.PersonDAOInterface;
import com.revature.sl.PersonServiceImp;
import com.revature.sl.PersonServiceInterface;
import io.javalin.Javalin;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class App {

    public static Logger logger = LogManager.getLogger(App.class);

    public static void main(String[] args) {

        // see the log notes in week 8 to get a list of logging level options
        logger.info("creating Javalin object now");
        Javalin app = Javalin.create(config ->{
            config.enableCorsForAllOrigins();
            config.enableDevLogging();
        });
        logger.info("Javalin object created!");

        /*
            This is where all three layers of the application come together. I create a dao object, then pass it
            into the service object, which I then pass into the controller object. This allows each layer of the
            application to transfer data from one layer to the next.
         */

        // this is coding to the interface: set the type as the interface, the object constructor used is from the implementation class
        PersonDAOInterface personDao = new PersonDAOImp();
        PersonServiceInterface personService = new PersonServiceImp(personDao);
        PersonController personController = new PersonController(personService);


        app.get("/", personController.sayHello);

        app.post("/person", personController.createPerson);

        app.get("/person/{id}", personController.getPerson);



        logger.info("Starting web server");
        app.start();



    }// main end

}
