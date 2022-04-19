package com.revature.calculator;

import com.revature.custom_exception.TheOneException;
import org.mockito.Mockito;
import org.mockito.internal.verification.VerificationModeFactory;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class CalculatorTests {

    public static Divider divider;
    public static Calculator calculator;

    @BeforeClass
    public void setup(){
        // we set up our divider object as a mock object using Mockito's mock method
        divider = Mockito.mock(Divider.class);
        calculator = new Calculator(divider);
    }

    @Test
    public void evenSuccess(){
        /*
            doReturn: the value you are returning from the stubbed method
            when: the mock object
            division: this is the method (and input) that is going to be stubbed
         */
        Mockito.doReturn(2).when(divider).division(14);
        String result = calculator.evenOdd(14);
        Assert.assertEquals(result, "Even");
    }

    @Test
    public void oddSuccess(){
        Mockito.doReturn(3).when(divider).division(12);
        String result = calculator.evenOdd(12);
        Assert.assertEquals(result,"Odd");
    }

    @Test
    public void handleTheOneExceptionCorrectly(){
        // use doThrow to throw an exception instead of returning a value
        Mockito.doThrow(new TheOneException("You can't divide by 1 with this method")).when(divider).division(1);
        String result = calculator.evenOdd(1);
        Assert.assertEquals(result,"You can't divide by 1 with this method");
    }

    @Test
    public void checkDivisionCalledOnce(){
        // this test makes sure that the division method is called one time with the argument 100
        Mockito.doReturn(50).when(divider).division(100);
        calculator.evenOdd(100);
        Mockito.verify(divider, VerificationModeFactory.times(1)).division(100);
    }

}
