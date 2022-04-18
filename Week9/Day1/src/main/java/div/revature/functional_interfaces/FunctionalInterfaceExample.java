package div.revature.functional_interfaces;

public class FunctionalInterfaceExample {
    /*
        How to create a lambda with a functional interface:
        FunctionalInterfaceBasics: reference the functional interface
        addition: give a variable name to the lambda implementation
        numOne: give a variable reference to the parameter
        ->: use an arrow notation to indicate you are now defining what the lambda will do
        numOne + 5: define your function
     */
    public static void main(String[] args) {
        // Here I defined what I actually want the lambda to do
        FunctionalInterfaceBasics addition = numOne -> numOne + 5;
        // here I reference the variable I assigned the lambda implementation to, called the method from the functional interface,
        // and passed in my argument
        System.out.println(addition.math(5));
        // below I create a new implementation of the math method and can see the results
        FunctionalInterfaceBasics subtraction = numOne -> numOne - 5;
        System.out.println(subtraction.math(5));

        // you must declare your return value in a multi-line lambda
        FunctionalInterfaceBasics multiLine = numOne -> {
            int result = numOne * 2;
            return result;
        };

    }
}
