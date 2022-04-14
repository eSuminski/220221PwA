package dev.revature.collections_basics;

import java.util.*;

public class SetBasics {
    /*
        Sets, unlike Lists, do not allow for duplicate values, and they also do not maintain the order of insertion.
        This type of collection serves more of a utility purpose: it is a useful tool for weeding out duplicate data, whether
        that data comes from a pre-made collection of data or you are creating a collection of content to be returned to
        the body of an HTTP response.
     */

    public static void main(String[] args) {
        Set<String> mythicalCreatures = new HashSet<>();
        mythicalCreatures.add("The Easter Bunny");
        mythicalCreatures.add("Santa Klaus");
        mythicalCreatures.add("The Queen of England");

        // the easiest way to access this content is to iterate through it
        for(String being:mythicalCreatures){
            // notice these are not in the order you placed them into the set
            System.out.println(being);
        }

        // a common practice is to pass the contents of another container through a set to get only the unique values
        int[] numbers = {1,2,2,3,3,4,5,5,6,6,6,7,8,9,9,10,10,10,10};
        List<Integer> myInts = new ArrayList<>();
        for(int x: numbers){
            myInts.add(x);
        }

        // this operation could also be handled by passing myInts into the constructor for the set as an argument
        Set<Integer> filter = new HashSet<>();
        filter.addAll(myInts);

        // like I do here
        List<Integer> filteredInts = new ArrayList<>(filter);

        /*
            Here I am going to use the Collections class, not to be confused with the Collection interface, to sort
            my list of filtered numbers, since I am not confident I will get them back in order. The Collections class
            has many helpful static methods for manipulating collections
         */
        Collections.sort(filteredInts);
        for(int x:filteredInts){
            System.out.println(x);
        }
    }
}
