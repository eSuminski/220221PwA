package div.revature.javalin;

import com.google.gson.Gson;
import io.javalin.http.Handler;

import java.util.ArrayList;
import java.util.List;

public class JavalinBasicsController {

    // this list and generator is supposed to represent a real database
    static List<Person> people = new ArrayList<>();
    static int personIdGenerator = 1;

    public JavalinBasicsController(){
        people.add(new Person(personIdGenerator,"Eric","Suminski"));
        personIdGenerator++;
    }

    public Handler helloWorld = ctx -> {
        ctx.result("Hello world!");
        ctx.status(200);
    };

    public Handler getPerson = ctx ->{
        // use the context object Javalin provides to read your path parameters
        int id = Integer.parseInt(ctx.pathParam("id"));
        for(Person p : people){
            if(p.getPersonId() == id){
                Gson gson = new Gson();
                String personJSON = gson.toJson(p);
                ctx.result(personJSON);
                ctx.status(200);
            }
        }
    };

    public Handler createPerson = ctx -> {
        // get the body of the request
        String body = ctx.body();
        // use gson to convert the json into an object that we need
        Gson gson = new Gson();
        Person person = gson.fromJson(body, Person.class);
        // this code here simulates sending the new object into your service/da layer
        person.setPersonId(personIdGenerator);
        personIdGenerator++;
        people.add(person);

        // return a result message
        ctx.result("Person added to list");
        ctx.status(201);
    };

    public Handler updatePersonById = ctx ->{
        // get body of request
        String body = ctx.body();

        // create object from body information
        Gson gson = new Gson();
        Person person = gson.fromJson(body, Person.class);

        // look for the object being changed in your database and adjust it
        for(Person p : people){
            if(p.getPersonId() == person.getPersonId()){
                int index = people.indexOf(p);
                people.set(index, person);
                String personJSON = gson.toJson(person);
                ctx.result(personJSON);
                ctx.status(200);
            }
        }
    };

    public Handler deletePersonById = ctx -> {
        int id = Integer.parseInt(ctx.pathParam("id"));
        int index = -1;
        for(Person p : people){
            if(p.getPersonId() == id){
                index = people.indexOf(p);
            }
        }
        if(index != -1){
            people.remove(index);
            ctx.result("Person removed");
            ctx.status(200);
        }

    };
}
