package dev.revature.custom_exceptions;

public class CustomUncheckedException extends RuntimeException{
    public CustomUncheckedException(String message){
        super(message);
    }

    public static void noTryCatchNeeded(){
        /*
            because this is an unchecked exception we do not need to handle it with a catch block. This type
            of exception is better suited for situations where you can't necessarily predict when or how this
            problem will arise (user error situation: you can't consistently predict if/when a user will do
            something wrong).
         */
        throw new CustomUncheckedException("i can throw this without a catch block to handle it");
    }

    public static void stillDontNeedTryCatch(){
        // despite this method only throwing the custom exception, we still don't need a try/catch block
        noTryCatchNeeded();
    }
}
