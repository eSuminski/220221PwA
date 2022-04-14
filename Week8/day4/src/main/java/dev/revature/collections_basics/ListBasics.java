package dev.revature.collections_basics;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class ListBasics {

    /*
        The primary objects you will work with from the List interface are the ArrayList and LinkedList. Both
        fundamentally do the same thing: they store objects in memory for you. HOW they do it is very different:
        ArrayLists are like a mutable array, whereas LinkedLists are more like nodes of storage that point to the next
        object in the list
     */

    public static void main(String[] args) {
        /*
            These collections make use of what is called Generics. Generics help provide type saftey for your Java
            code by indicating what kind of objects will be stored in your container. For the containers below, they
            will be storing String objects, which is indicated by the Object inside the diamond brackets by the type
            declarations
         */
        List<String> myArrayList = new ArrayList<>();
        List<String> myLinkedList = new LinkedList<>();


        // you can freely add and remove content from these collections

        // add
        myArrayList.add("Hello World!");
        myArrayList.add("Hello World!"); // duplicates are allowed
        myArrayList.add("It's a beautiful day in the neighborhood");
        myLinkedList.add("Hello World");
        myLinkedList.add("Hello World"); // duplicates are allowed
        myLinkedList.add("It's a beautiful day in the neighborhood");

        // remove
        myArrayList.remove("Hello World!");
        myLinkedList.remove("Hello World!");

        // there is also a clear option
        myArrayList.clear();
        myLinkedList.clear();

        // you can use indexing to access the contents of both lists
        myArrayList.add("Hello World!");
        myArrayList.add("It's a beautiful day in the neighborhood");
        myLinkedList.add("Hello World");
        myLinkedList.add("It's a beautiful day in the neighborhood");

        System.out.println(myArrayList.get(0));
        System.out.println(myLinkedList.get(0));

        /*
            So how to decide which option to use? It depends on what you are trying to do: if you need to access
            specific content in your list then you should use an ArrayList. However, if you're not concerned with
            accessing specific content and just need to add/remove content quickly to the front or back of the list,
            then a LinkedList would be better for you. See below for a time test between the two
         */

        testArrayListvsLinkedList();

    }

    public static void testArrayListvsLinkedList(){
        // you can swap between arrayList and linkedList to see how they differ
        // searching is easier in ArrayLists, adding elements is easier in LinkedLists
        List<Object> arrayList = new ArrayList<>();
        List<Object> linkedList = new LinkedList<>();

        /*
            my test-run times
            arrayList:
                .008 seconds to add 100k objects to end of list
                .002 seconds to get the object at index position 50000
                2.016 seconds to add 100k objects to start of list
            linkedList:
                .007 seconds to add 100k objects to end of list
                8.763 seconds to get the object at index position 50000
                .005 seconds to add 100k objects to start of list
         */

        List<Object> testList = arrayList; // change this to linkedList to see the LinkedList times

        long start = System.nanoTime();
        for(int i =0; i<100_000; i++){
            testList.add(new Object()); // adding 100,000 objects to the END of the list
        }
        long end = System.nanoTime();
        System.out.println("Time to add 100,000 objects to the end " + (end-start)/1000000000.0);

        start = System.nanoTime();
        for(int i =0; i<100_000; i++){
            testList.get(50_000); // get object at middle of list
        }
        end = System.nanoTime();
        System.out.println("Time to get object 50_000 in the middle of the list " + (end-start)/1000000000.0);

        start = System.nanoTime();
        for(int i =0; i<100_000; i++){
            testList.add(0, new Object()); // add to the beginning of the list 100_000 times
        }
        end = System.nanoTime();
        System.out.println("Time to add object 100_000 to the beginning of the list " + (end-start)/1000000000.0);
    }
}
