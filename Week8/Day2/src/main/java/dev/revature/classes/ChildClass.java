package dev.revature.classes;

// use the extends keyword to indicate your class inherits from a parent class
public class ChildClass extends ParentClass{
    // you can define fields that are specific to the child class
    String childString;
    public ChildClass(String parentString, String childString) {
        // the super keyword is used to pass arguments to the parent constructor
        super(parentString);
        // use this and the child specific field name to set the value for the child specific fields
        this.childString = childString;
    }

    public static void main(String[] args) {
        ChildClass child = new ChildClass("this is the parent string", "this is the child string");
        System.out.println(child.parentString);
        System.out.println(child.childString);
    }
}
