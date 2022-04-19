package com.revature.divider;

import com.revature.calculator.Divider;
import com.revature.custom_exception.TheOneException;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class DividerTests {

    public static Divider divider;

    @BeforeClass
    public static void setup(){
        divider = new Divider();
    }

    @Test
    public void divideSuccessfully(){
        Assert.assertEquals(divider.division(10), 5);
    }

    // this is a simple way to test your expected exceptions
    @Test(expectedExceptions = TheOneException.class, expectedExceptionsMessageRegExp = "You can't divide by 1 with this method")
    public void throwTheOneExceptionSuccessfully(){
        divider.division(1);
    }

}
