# Java Week 9

## Functional Interfaces / Lambdas
A Functional interface is an interface with one abstract method which is used to implement lambdas. A Lambda is a way of doing functional(esque) programming in Java. It follows the pattern: parameter/s -> expression
```java
@FunctionalInterface // make sure to add this annotation to your interface to make it a funcitonal one
public interface PrintNameFunctionalInterface {

    int printName(String name);
}

public class FunctionalInterfaceExample {

    public static void main(String[] args) {
        // Here I define what I actually want the lambda to do
        PrintNameFunctionalInterface tom = name -> System.out.println(name);
        tom.printName("tom");

        // use {} if your lambda has more than one line of code
        PrintNameFunctionalInterface sally = name -> {
            String value = name;
            System.out.println(value);
            };
        sally.printName("sally");
    }
}

```

## Javalin / GSON
Javalin is a framework that handles creating a web server for our application, which receives HTTP requests and returns HTTP responses for us. It makes use of a functional interface called Handler to craft the response. We can make use of the GSON class to handle converting data from a JSON into our Java classes, and vice versa

dependencies needed in the pom:
```xml
        <!-- https://mvnrepository.com/artifact/io.javalin/javalin -->
        <dependency>
            <groupId>io.javalin</groupId>
            <artifactId>javalin</artifactId>
            <version>4.5.0.RC0</version>
        </dependency>
        <dependency>
        <!-- this one is needed for javalin logging -->
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-simple</artifactId>
            <version>1.7.31</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/com.google.code.gson/gson -->
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.9.0</version>
        </dependency>
```

controller setup: see Week9 Day1 folder in repo

Javalin object setup: see Week9 Day1 folder in repo

## Mockito
Mockito is a class we can use to stub and mock our test results in Java. The class has some built-in methods to handle stubbing and mocking:
- doReturn() allows you to stub the results of a method
- doThrow() is the same as doReturn, except an exception is thrown instead
- when() is used to determine what mocked object is being stubbed
    - example: Mockito.doReturn(5).when(mockedObject).methodBeingStubbed(argumentGoesHere);
-verify() can be used to check the path of execution for a method
    - example: Mockito.verify(mockedObject, VerificationFactory.times(1)).methodBeingStubbed(argumentGoesHere)

See Week9 Day2 in repo for more details on setting up/using Mockito

## Selenium & Cucumber
Cucumber is the testing framework we use with Java to do End to End Testing. It works well with Selenium to automate the steps a user would take in your application. The test is controlled by a class called TestRunner, which you need to set up with your drivers, poms, and WebDriverWaits in order for your tests to be successful.
### Cucumber test steps
1. Create User Stories/Acceptance Criteria
2. Create Application (use BDD and TDD)
3. Create Feature Files based off Acceptance Criteria
    - 3.2 make sure to include alternate path scenarios where applicable
4. Create your TestRunner class
5. Create your Poms
6. Create your Step implementation classes
    - 6.2 you can run your TestRunner before the steps are implemented to auto generate your steps
7. Run your tests and adjust as needed

see Week9 Day3 for examples of how to build your TestRunner, Poms, and Steps
