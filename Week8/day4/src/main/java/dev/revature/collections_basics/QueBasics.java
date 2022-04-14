package dev.revature.collections_basics;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.PriorityQueue;
import java.util.Queue;

public class QueBasics {
    /*
        Ques are particularly useful when you want to follow a first in, first out rule for your collection
     */

    public static void main(String[] args) {
        // this queue has initial capacity for 10 objects
        Queue<String> myQueue = new PriorityQueue<>();
        myQueue.add("Eric");
        myQueue.add("Sam");
        myQueue.add("Luke");

        // this returns the head element of the queue, but does not remove it
        myQueue.peek();

        // this returns AND removes the head element of the que, changing the head to the next object in line
        myQueue.poll();

        /*
            A Queue can be useful if you want to control what elements you interact with in an orderly fashion. You
            could also use a Deque object to gain access to both the front and back of the list
         */



    }
}
