# Cucumber/Selenium Review
### Cucumber
Cucumber is a testing framework that allows you to easily create End to End tests that utilize gherkin syntax. This framework can take your acceptance criteria (found in one or more feature files) and link them to test steps you create in test classes (typically placed inside of a steps package). Once you have your steps definied (not implemented) you can then write the code to make sure your acceptance criteria is being fullfilled. What Cucumber does specifically is link your acceptance criteria with the step implementations you create in your test classes.
```feature
Feature: As a user I should be able to view Wikipedia pages in different languages
  Scenario: As an English user I should be able to view Wikipedia in English
    Given I am on the Wikipedia home page
    When  I click the English link
    Then  I should be on the English home page
  Scenario: As an Spanish user I should be able to view Wikipedia in Spanish
    Given I am on the Wikipedia home page
    When  I click the Spanish link
    Then  I should be on the Spanish home page
  Scenario: As an Italian user I should be able to view Wikipedia in Italian
    Given I am on the Wikipedia home page
    When  I click the Italian link
    Then  I should be on the Italian home page
```
Cucumber takes the acceptance criteria above and links it to the steps defined below. The means by which we have been doing this is a TestRunner class provided by Junit
```java
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import java.io.File;
import java.time.Duration;

@RunWith(Cucumber.class) // this sets Cucumber as the framework to run our tests
@CucumberOptions(
        /*
            features: this determines which feature file/s will be used
            glue: this tells Cucumber where the step implementations are. Direct it to a package
            plugin: this is an optional setting we use to generate a nice html report of the test results
         */
        features = {"src/test/resources/features"},
        glue = "com/revature/steps",
        plugin = {"pretty","html:src/test/resources/reports/html-e2e-report.html"}
)
public class TestRunner {

    /*
        The WebDriver field below is necessary for interacting with webpages: it has nothing to do inherently with Cucumber, but you will need it to make use of Selenium: see notes below for Selenium information
    */
    public static WebDriver driver;


    @BeforeClass
    public static void setup(){
        // use the three lines below to set your driver: see Selenium notes below for more information
        File file = new File("src/test/resources/chromedriver.exe"); // this tells Java where the driver is located
        System.setProperty("webdriver.chrome.driver", file.getAbsolutePath()); // this tells Java what kind of driver you are using, and where it is located
        driver = new ChromeDriver(); // this initializes the value of the driver field you created above
    }

    // don't forget to quit your driver when you are done
    @AfterClass
    public static void teardown(){
        driver.quit();
    }

}

```
```java
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class WikiLinksSteps {

    @Given("I am on the Wikipedia home page")
    public void i_am_on_the_wikipedia_home_page() {
        // you write code here to simulate a user's actions
    }
    @When("I click the English link")
    public void i_click_the_english_link() {
        // you write code here to simulate a user's actions
    }
    @Then("I should be on the English home page")
    public void i_should_be_on_the_english_home_page() {
        // you write code here to simulate a user's actions
    }

    @When("I click the Spanish link")
    public void i_click_the_spanish_link() {
        // you write code here to simulate a user's actions
    }
    @Then("I should be on the Spanish home page")
    public void i_should_be_on_the_spanish_home_page() {
        // you write code here to simulate a user's actions
    }

    @When("I click the Italian link")
    public void i_click_the_italian_link() {
        // you write code here to simulate a user's actions
    }
    @Then("I should be on the Italian home page")
    public void i_should_be_on_the_italian_home_page() {
        // you write code here to simulate a user's actions
    }

}
```
Note in the above: All Cucumber has done is link the feature file steps with the Java code steps by using the TestRunner class: you as the tester must provide the means of actually implementing the steps. I skipped ahead a bit and added the Driver field to the TestRunner class already: Selenium will make use of it to interact with the webpage.
### Selenium
Selenium is a browser automation tool: that's it (see their website). That being said, Selenium is the perfect tool to pair with cucumber to create End to End tests for web applications, since Selenium can fill in for a real person interacting with your web pages. In the above examples we linked our acceptance criteria with our code steps, but we had no means of simulating a user on Wikipedia. This is where Selenium comes in: we can use it to simulate the actions a user would take browsing the web. Since the driver has already been set up in the TestRunner we can implement our steps via Selenium in the WikiLinksSteps class
```java
package com.revature.steps;

import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.junit.Assert;

public class WikiLinksSteps {

    @Given("I am on the Wikipedia home page")
    public void i_am_on_the_wikipedia_home_page() {
        // the get method is used to simulate the user typing a url into the browser
        TestRunner.driver.get("https://www.wikipedia.org/");
    }
    @When("I click the English link")
    public void i_click_the_english_link() {
        // the findElement method is used to locate an element on the DOM. You first use the By class to determine the css selector you are using, and the second argument is the selector value
        WebElement englishLink = TestRunner.driver.findElement(By.id,"js-link-box-en");
        // the click method is used to simulate the user clicking on a web element
        englishLink.click();
        
    }
    @Then("I should be on the English home page")
    public void i_should_be_on_the_english_home_page() {
        // the getTitle method is used to retrieve the title of the webpage you are on
        String title = TestRunner.driver.getTitle();
        // here we are using the Assert class from Junit to make sure we are on the correct page, else the step will fail because the assertEquals method will throw an exception
        Assert.assertEquals("Wikipedia, the free encyclopedia", title);
    }

    @When("I click the Spanish link")
    public void i_click_the_spanish_link() {
        WebElement spanishLink = TestRunner.driver.findElement(By.cssSelector,"div[lang='es']");
        spanishLink.click();
    }
    @Then("I should be on the Spanish home page")
    public void i_should_be_on_the_spanish_home_page() {
        Assert.assertEquals("Wikipedia, la enciclopedia libre", TestRunner.driver.getTitle());

    }

    @When("I click the Italian link")
    public void i_click_the_italian_link() {
        // note I can directly call click() on the result of findElement()
        TestRunner.driver.findElement(By.xpath,"/html/body/div[2]/div[8]/a").click();
    }
    @Then("I should be on the Italian home page")
    public void i_should_be_on_the_italian_home_page() {
        Assert.assertEquals("Wikipedia, l'enciclopedia libera", TestRunner.driver.getTitle());
    }

}
```
Notice that Selenium itself is not doing any testing: it is simply simulating the actions of a user. Cucumber is checking to see if an exception is thrown in any of the steps, and if they are, then it marks the step as failing. 

This code is fine, but for larger tests it can be a hassle having to write all of the code inside of the steps themselves: this also makes any potential refactors to the test more difficult, because you would need to comb through the steps to find all the places where any affected code is located and then manually change each individual place. To avoid this problem, and to avoid general boilerplate code, you can create a Page Object Model for each webpage you simulate interacting with, which will localize all the web elements you need to interact with, making it both easier to interact with elements, and also easier to refactor your code when necessary.
```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class WikiHome {

    private WebDriver driver;

    public WikiHome(WebDriver driver){
        // a driver is necessary for finding the web elements you need to interact with. You can initialize this field in the TestRunner
        this.driver = driver;
        // the page factory abstracts away the logic for interacting with web elements: you use the @FindBy annotation to indicate how to find the web elements you need
        PageFactory.initElements(driver,this);
    }

    // we use FindBy to tell the page factory what selector and associated values to use to find the element we want
    @FindBy(id = "js-link-box-en")
    public WebElement english;

    @FindBy(css = "div[lang='es']")
    public WebElement spanish;

    @FindBy(xpath = "/html/body/div[2]/div[8]/a")
    public WebElement italian;

}
```
With the pom created you can add it to the TestRunner class to make use of it in your step implementation
```java
import com.revature.poms.WikiHome;
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import java.io.File;


@RunWith(Cucumber.class)
@CucumberOptions(
        features = {"src/test/resources/features"},
        glue = "com/revature/steps",
        plugin = {"pretty","html:src/test/resources/reports/html-e2e-report.html"}
)
public class TestRunner {

    public static WebDriver driver;
    public static WikiHome wikiHome;


    @BeforeClass
    public static void setup(){
        File file = new File("src/test/resources/chromedriver.exe");
        System.setProperty("webdriver.chrome.driver", file.getAbsolutePath());
        driver = new ChromeDriver();

        // don't forget to pass your driver into your poms
        wikiHome = new WikiHome(driver);
    }

    // don't forget to quit your driver when you are done
    @AfterClass
    public static void teardown(){
        driver.quit();
    }

}
```
Now that your pom is initialized in the TestRunner you can use it in your steps
```java
package com.revature.steps;

import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;

public class WikiLinksSteps {

    @Given("I am on the Wikipedia home page")
    public void i_am_on_the_wikipedia_home_page() {
        TestRunner.driver.get("https://www.wikipedia.org/");
    }
    @When("I click the English link")
    public void i_click_the_english_link() {
        TestRunner.wikiHome.english.click();
    }
    @Then("I should be on the English home page")
    public void i_should_be_on_the_english_home_page() {
        String title = TestRunner.driver.getTitle();
        Assert.assertEquals("Wikipedia, the free encyclopedia", title);
    }

    @When("I click the Spanish link")
    public void i_click_the_spanish_link() {
        TestRunner.wikiHome.spanish.click();
    }
    @Then("I should be on the Spanish home page")
    public void i_should_be_on_the_spanish_home_page() {
        Assert.assertEquals("Wikipedia, la enciclopedia libre", TestRunner.driver.getTitle());
    }
    @When("I click the Italian link")
    public void i_click_the_italian_link() {
        TestRunner.wikiHome.italian.click();
    }
    @Then("I should be on the Italian home page")
    public void i_should_be_on_the_italian_home_page() {
        Assert.assertEquals("Wikipedia, l'enciclopedia libera", TestRunner.driver.getTitle());
    }
}
```
Now any potential changes to your webpage can be handled in the pom (like an id being changed, an element being replaced with another, etc) and your steps can remain the same.
### Conclusion
- Cucumber
    - a testing framework that can turn your Acceptance Criteria into executable steps
    - Alone it does NOT provide the means of interacting with your web pages
- Selenium
    - a web browser automation tool
    - you can simulate user actions on the web using Selenium, but it does not provide any inherent testing features
    - [This is the documentation for Selenium: it contains more specific methods you can use to automate user actions](https://www.selenium.dev/documentation/overview/)

- Cucumber and Selenium together
    - You use Cucumber to determine the steps a user would take for your E2E tests
    - You use Selenium to automate the actions a user would do on your webpages 
- Page Object Model
    - a design pattern used to reduce boilerplate code and simplify the refactoring of your E2E tests.
    - you write the code to locate your elements in the pom, then reference them via a pom object in the steps
        - you could even go as far as to create methods which perform the desired action upon the element, and then call the method in your step implementation
- Junit
    - a test framework that integrates well with Cucumber
    - we make use of the Junit BeforeClass and AfterClass decorators to set up and tear down our E2E test
        - Cucumber looks for a class called TestRunner to perform the setup and teardown when integrated with Junit