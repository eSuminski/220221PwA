package com.revature.challenges.medium;

public class ChallengeOne {
    /*
        create the code for the static convert method below that will change the naming convention style of a variable
        into a new one. Example:
        convert("Pascal","Snake","VariableOne) should produce: variable_one
        Your method should be able to handle Pascal, Snake, and Camel case naming conventions. Do not hard code your
        answers: this coding challenge was designed to force you to accommodate complex requirements
     */
    /*
        hint: ASCII can be your friend here
     */

    public static void main(String[] args) {
        String[][] entries = {
                {"Pascal", "Snake", "VariableOne"},
                {"Pascal", "Camel", "VariableTwo"},
                {"Camel", "Snake", "variableThree"},
                {"Camel", "Pascal","variableFour"},
                {"Snake", "Camel", "variable_five"},
                {"Snake", "Pascal", "variable_six"}
        };
        for(String[] entry : entries){
            convert(entry[0],entry[1], entry[2]);
        }


    }

    // write your code below
    static void convert(String startingCase, String endingCase, String variableName){

    }

}
