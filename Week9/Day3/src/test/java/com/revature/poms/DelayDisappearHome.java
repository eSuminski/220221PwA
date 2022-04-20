package com.revature.poms;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class DelayDisappearHome {
    private WebDriver driver;

    public DelayDisappearHome(WebDriver driver){
    this.driver = driver;
        PageFactory.initElements(driver,this);
    }

    @FindBy(id = "button")
    public WebElement button;
}
