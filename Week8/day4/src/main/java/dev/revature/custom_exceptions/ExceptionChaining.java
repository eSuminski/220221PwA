package dev.revature.custom_exceptions;



public class ExceptionChaining {
    public static void main(String[] args) {
        try{
            System.out.println("You can chain multiple catch blocks");
        // you can have one catch block handle multiple exceptions, seperate the possible exceptions with a | character
        // you could also make multiple catch blocks if you want to handle exceptions in different ways
        } catch(Exception|Error e){
            System.out.println(e.getMessage());
        } finally{
            System.out.println("this finally block will always run, unless the application crashes or is exited");
        }
    }
}
