package dev.revature.methods;

public class MethodsBasics {

    public static void main(String[] args){
        MethodsBasics obj = new MethodsBasics();
        obj.sayHelloWorld();
        staticSayHelloWorld();
        System.out.println(obj.addition(10,10));
        System.out.println(obj.addition("Hello ", "world!"));
    }

    // this method is attatched to objects of my class: to call it I must first create an object of the class, then I can use it
    public void sayHelloWorld(){
        System.out.println("Hello world!");
    }

    // this method is attached to the class: you don't have to create an object of the class to use it
    public static void staticSayHelloWorld(){
        System.out.println("Hello world!");
    }

    // this is overloading: despite having the same method name, the return types and parameters are different
    public int addition(int numOne, int numTwo){
        return numOne + numTwo;
    }

    public String addition(String one, String two){
        return one + two;
    }
}
