package com.revature.calculator;

import com.revature.custom_exception.TheOneException;

public class Calculator {

    public Divider divider;

    public Calculator(Divider divider) {
        this.divider = divider;
    }

    public String evenOdd(int num){
        try{
            int result = divider.division(num);
            if(result%2==0){
                return "Even";
            } else {
                return "Odd";
            }
        } catch (TheOneException e){
            return e.getMessage();
        }
    }

}
