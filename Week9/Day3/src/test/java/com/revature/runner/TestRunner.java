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

@RunWith(Cucumber.class)
@CucumberOptions(
        features = {"src/test/resources/features/UsingWaits.feature"},
        glue = "com/revature/steps",
        plugin = {"pretty","html:src/test/resources/reports/html-e2e-report.html"}
)
public class TestRunner {

    public static WebDriver driver;
    public static WikiHome wikiHome;
    public static DelayDisappearHome ddHome;
    public static WebDriverWait wait;


    @BeforeClass
    public static void setup(){
        File file = new File("src/test/resources/chromedriver.exe");
        System.setProperty("webdriver.chrome.driver", file.getAbsolutePath());
        driver = new ChromeDriver();
        wikiHome = new WikiHome(driver);
        ddHome = new DelayDisappearHome(driver);
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(1));
        wait = new WebDriverWait(driver,Duration.ofSeconds(4));
    }

    @AfterClass
    public static void teardown(){
        driver.quit();
    }

}
