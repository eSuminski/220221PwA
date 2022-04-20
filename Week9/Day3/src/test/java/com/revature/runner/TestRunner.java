package com.revature.runner;

import com.revature.poms.DelayDisappearHome;
import com.revature.poms.WikiHome;
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;
import java.time.Duration;
/*
    this class is what will handle running your E2E tests in Java. Make sure it is called TestRunner, because
    Cucumber will be looking for a class with that name to handle the setup and teardown for the test
 */

@RunWith(Cucumber.class) // this sets Cucumber as the framework to run our tests
@CucumberOptions(
        /*
            features: this determines which feature file/s will be used
            glue: this tells Cucumber where the step implementations are. Direct it to a package
            plugin: this is an optional setting we use to generate a nice html report of the test results
         */
        features = {"src/test/resources/features/UsingWaits.feature"},
        glue = "com/revature/steps",
        plugin = {"pretty","html:src/test/resources/reports/html-e2e-report.html"}
)
public class TestRunner {

    /*
        make your fields public static: at minimum you need a driver, make sure to add any poms here as well.
        You will also want to add any WebDriverWaits
     */

    public static WebDriver driver;
    public static WikiHome wikiHome;
    public static DelayDisappearHome ddHome;
    public static WebDriverWait wait;


    @BeforeClass
    public static void setup(){
        // use the three lines below to set your driver
        File file = new File("src/test/resources/chromedriver.exe");
        System.setProperty("webdriver.chrome.driver", file.getAbsolutePath());
        driver = new ChromeDriver();

        // don't forget to pass your driver into your poms
        wikiHome = new WikiHome(driver);
        ddHome = new DelayDisappearHome(driver);

        // make sure to set your implicit wait and any explicit waits you need
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(1));
        wait = new WebDriverWait(driver,Duration.ofSeconds(4));
    }

    // don't forget to quit your driver when you are done
    @AfterClass
    public static void teardown(){
        driver.quit();
    }

}
