package com.suminski.playground;

public class ControlFlow {
    public static void main(String[] args){
        /*
        control flow:
        key-word(statement)
         */

        int x = 7;
        int y = 7;

        if(x < y){
            System.out.println("x is less than y");
        } else if (x > y){
            System.out.println("x is greater than y");
        } else {
            System.out.println("x and y are the same");
        }

        // for (initialize a value; create loop condition; change value)
        for(int i = 0; i <= 10; i = i + 1){
            System.out.println(i);
        }

        for(int i = 0; i<5; i = i + 1){
            for(int a = 0; a <5;a++){
                System.out.println("This print statement is in outter loop " + i +" and inner loop " + a);
            }
        }

        int b = 0;
        while(b<5){
            // ++b will increment b and then print the statement, b++ will print the statement then increment b
            System.out.println("I am printing number" + ++b);
        }

        int c = 10;
        do{
            // this will print even though the boolean condition below is false
            System.out.println("I am printing only numbers 1-9: " + c);
        } while(c<10);



    } // closing bracket for main
}
