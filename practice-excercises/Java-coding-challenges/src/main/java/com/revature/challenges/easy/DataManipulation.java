package com.revature.challenges.easy;

public class DataManipulation {

    /*
        Your challenge is to sort the numbers of each array below from smallest to largest and print them to the
        console. Write your code in the given sortNumbers static method

        Do not hard-code your answers: the goal of this exercise is to help you become better at problem-solving,
        and to help you become more familiar with working with data collections.
     */
    /*
        expected outcome:
        [0, 1, 2, 2, 3, 11, 23, 34, 43, 55, 56, 78, 3245]
        [3, 4, 21, 23, 32, 44, 65, 67, 78, 100, 280, 300]
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        [20, 30, 40, 50, 60, 70, 80, 90, 100, 101]
     */

    public static void main(String[] args) {
        int[][] nums ={
                {1,2,11,3,43,23,2,55,3245,0,34,56,78},
                {3,67,32,4,23,65,78,100,280,300,44,21},
                {1,2,3,4,5,7,6,8,9,10},
                {100,90,80,70,60,50,40,30,20,101}
        };
        for(int[] numbers : nums){
            sortNumbers(numbers);
        }

    }

    static void sortNumbers(int[] nums){

    }

}
