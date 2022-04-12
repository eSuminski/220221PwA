package dev.revature.scopes;

public class Scopes {
    // a static variable belongs to the class scope
    static String one;
    // a non-static variable belongs to the instance scope (the individual object itself)
    String two;

    public static void main(String[] args) {
        Scopes obj = new Scopes();
        Scopes objTwo = new Scopes();
        // to change the variable in the class scope you reference the class, not objects
        Scopes.one = "this is now the value of field one";
        // to change the variables in the instance scope you reference the objects directly
        obj.two = "this is now the value of field two for object one";
        objTwo.two = "this is now the value of field two for object two";
        methodBlockScope();
        // I can't access the x or i variables from the methodBlockScope method outside of the method
    }

    public static void methodBlockScope(){
        // this x variable is part of the method scope: it is accessible in the method, and exists until the method is done
        int x = 10;
        // this i variable is part of the block scope of the for loop: it only exists and is accessible within the block of code
        for(int i = 0; i < x; i++){
            System.out.println(i);
        }
    }
}
