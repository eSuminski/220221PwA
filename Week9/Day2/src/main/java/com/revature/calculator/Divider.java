package com.revature.calculator;

import com.revature.custom_exception.TheOneException;

public class Divider {

    public int division(int num){
        if(num==1){
            throw new TheOneException("You can't divide by 1 with this method");
        }
        return num/2;
    }

}
