package dev.revature.classes;

public class BasicClassInfo {
    int myInt;
    String myString;
    boolean myBoolean;

    // Java will provide a no-args constructor by default if no other constructor is defined
    public BasicClassInfo(){}

    // if you define your own constructor/s you lose access to the default no-args constructor
    public BasicClassInfo(int myInt, String myString, boolean myBoolean){
        this.myInt = myInt;
        this.myString = myString;
        this.myBoolean = myBoolean;
    }


    public static void main(String[] args) {
        BasicClassInfo myObject = new BasicClassInfo(10,"my string", true);
        BasicClassInfo myNewObject = new BasicClassInfo(); // if we don't define the no-args constructor above this will not work

    }
}
