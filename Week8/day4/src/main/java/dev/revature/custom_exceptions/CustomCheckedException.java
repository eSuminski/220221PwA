package dev.revature.custom_exceptions;

/*
    this custom exception is a checked exception: any code that can produce this exception must be placed in a
    try/catch block.

    The exception to this rule is if the method that could create this exception "throws" the exception. This
    informs Java that we are aware of the potential exception and will handle it in a different part of our code
 */
public class CustomCheckedException extends Exception{
    public CustomCheckedException(String message){
        super(message);
    }

    public static void thisNeedsATryCatchBlock(){
        try {
            if (false) {
                System.out.println("This will not run, since a false if statement will not trigger");
            } else {
                throw new CustomCheckedException("this is the message for the exception");
            }
        } catch(CustomCheckedException e){
            // because our CustomCheckedException is a checked exception we have to handle it with a catch block
            System.out.println(e.getMessage());
        }
    }

    public static void thisDoesNotNeedATryCatchBlock() throws CustomCheckedException{
        /*
            because we added the throws keyword to the method signature and stated our checked exception
            CustomCheckedException is thrown by the method, we no longer need the try/catch block to handle
            this exception here in the method. We will, however, need to handle it wherever this method gets
            called (see below). This is called "ducking" the method
         */
        throw new CustomCheckedException("We can get this message by calling the catchingDuckedException method");
    }

    public static void catchingDuckedException(){
        try{
            // because this method throws CustomCheckedException we have to have a catch block to handle the exception
            thisDoesNotNeedATryCatchBlock();
        } catch(CustomCheckedException e){
            System.out.println(e.getMessage());
        }
    }
}
