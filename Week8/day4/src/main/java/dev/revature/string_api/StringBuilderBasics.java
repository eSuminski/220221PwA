package dev.revature.string_api;

public class StringBuilderBasics {
    /*
        You can think of a StringBuilder object as a malleable string: objects of this class are not stored in the
        string pool, but these objects do allow you to persist changes easily to a string-like object
     */

    public static void main(String[] args) {
        StringBuilder myStringBuilder = new StringBuilder("this is my text");
        // this will print our phrase like a regular string
        System.out.println(myStringBuilder);

        // the easiest way to change your string is to append new content to it. The print statement will reflect the changes
        myStringBuilder.append(" which I have now edited");
        System.out.println(myStringBuilder);

        // this will reverse the order of the characters
        myStringBuilder.reverse();
        System.out.println(myStringBuilder);
    }

    /*
        There are many other functions you can use on a StringBuilder object, all of which provide ways of either
        transforming the StringBuilder object or parsing the content of the object.

        StringBuilder objects are more resource intensive than regular strings, so stick with a regular string
        unless you know you are going to be manipulating the string constantly (like in a coding challenge)
     */

}
