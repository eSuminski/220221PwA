package div.revature.javalin;

import io.javalin.Javalin;

public class JavalinBasics {
    /*
        We will be using Javalin to handle receiving HTTP requests and returning HTTP responses.
     */

    public static void main(String[] args) {
        Javalin app = Javalin.create(config -> {
            config.enableCorsForAllOrigins();
            config.enableDevLogging();
        });

        JavalinBasicsController controller = new JavalinBasicsController();

        app.get("/", controller.helloWorld);

        app.get("/person/{id}", controller.getPerson);

        app.post("/person", controller.createPerson);

        app.put("/person", controller.updatePersonById);

        app.delete("/person/{id}", controller.deletePersonById);

        app.start();

    } // main end
}
