package dev.revature.collections_basics;

import java.util.HashMap;
import java.util.Map;

public class MapBasics {
    /*
        Maps are how you store key:value pairs in your Java code. The type of map we will focus on is a HashMap
     */

    public static void main(String[] args) {
        Map<Integer,String> myMap = new HashMap<>();

        // use put to add a key/value pair
        myMap.put(1,"Eric");

        // getOrDefault will either get the value of your key, or return a default value if the key doesn't exist
        myMap.getOrDefault(2,"No value found for key 2");

        // get will return the value of the key
        myMap.get(1);

        // values will return a list of all values in the map
        myMap.values();

        // keySet will return a set of the keys in the map
        myMap.keySet();

        // containsKey will return a boolean dependent on whether the key exists in the map
        myMap.containsKey(1);

        // containsValue does the same but for a value
        myMap.containsValue("Billy");
    }
}
