package dev.revature.arrays;

public class ArrayBasics {

    /*
        An Array is a basic container that can store other objects. It is immutable once created, and the elements
        inside can be accessed via their index position.
     */

    public static void main(String[] args) {
        /*
            The first array is created with integers 1-5 already inside. The second array is empty but has five
            positions inside that can store integers
         */
        int[] myIntArray1 = {1, 2, 3, 4, 5};
        int[] myIntArray2 = new int[5];
        myIntArray2[0] = 6;
        myIntArray2[1] = 7;
        myIntArray2[2] = 8;
        myIntArray2[3] = 9;
        myIntArray2[4] = 10;

        // this will print the contents of the first array one by one
        for (int x = 0; x < myIntArray1.length; x++) {
            System.out.println(myIntArray1[x]);
        }
        // and this the second array
        for (int x : myIntArray2) {
            System.out.println(x);
        }

        usingVarArg(1,2,3,4,5,6,7,8,9,10); // see notes below
    }
        /*
            The primary place you will see basic arrays is when they are used for a method's variable argument. This
            happens when you are unsure of how many parameters you will be working with, so a var-arg is Java's way
            of saying "this parameter is going to be an array of all the arguments provided". The var-arg must be
            the last declared parameter
         */
    //this could also be written as : public static void usingVarArg(int[] nums){}
    public static void usingVarArg(int...nums){
        for(int x:nums){
            System.out.println(x);
        }
    }
}

