package com.revature.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class WikiHome {

    private WebDriver driver;
    private By searchBar = By.id("searchInput");
    private By searchButton = By.className("pure-button");

    public WikiHome(WebDriver driver){
        this.driver = driver;
        // the page factory abstracts away the logic for interacting with web elements
        PageFactory.initElements(driver,this);
    }

    // we use FindBy to tell the page factory what selector and associated values to use to find the element we want
    @FindBy(id = "js-link-box-en")
    public WebElement english;

    @FindBy(css = "div[lang='es']")
    public WebElement spanish;

    @FindBy(xpath = "/html/body/div[2]/div[8]/a")
    public WebElement italian;

    // you can also avoid using the page factory and manually search for the elements youtself
    public void sendKeysToSearchbar(String input){
        driver.findElement(searchBar).sendKeys(input);
    }

    public void clickSearchButton(){
        driver.findElement(searchButton).click();
    }

}
