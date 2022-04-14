package dev.revature.string_api;

public class BasicString {
    /*
        Strings in Java are immutable objects: once set they can not be changed. The way Java stores these values
        is a little different from other objects: in the heap (see study guide) there is a section called the
        string pool where all strings are stored. Because many strings are reused, any time you create a reference
        to a string that already exists the variable will point to the same string object in the string pool as your
        previous references did.
     */

    public static void main(String[] args) {
        String stringOne = "this is one object";
        String stringTwo = "this is one object";
        System.out.println(stringOne.equals(stringTwo)); // this will return true: the content of each string is the same
        System.out.println(stringOne == stringTwo); // this will also return true: they are pointing to the same string object in the string pool
        /*
            note the difference between the equals method and the equality operator: the equals method checks the content
            of the strings, the equality operator checks the memory location of the strings. To create a new string object
            with the same content you have to use the new keyword and the String constructor
         */

        String stringThree = new String("this is one object");
        System.out.println(stringOne.equals(stringThree));// this will return true: the content is the same
        System.out.println(stringOne == stringThree); // this will return false: the two objects are stored in different memory locations
    }

    /*
        use basic strings when you just need to store a message or characters for use later. If you are going to
        perform any sort of complex operations with the string you are better off using a StringBuilder class
     */
}
