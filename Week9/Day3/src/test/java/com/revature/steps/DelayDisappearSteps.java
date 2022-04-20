package com.revature.steps;

import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class DelayDisappearSteps {

    @Given("I am on the delay-disappear page")
    public void i_am_on_the_delay_disappear_page() {
        TestRunner.driver.get("File:C:\\Users\\EricSuminski\\Desktop\\220221PwA\\Week9\\Day3\\src\\test\\resources\\delay-disappear.html");
    }
    @When("I click the button")
    public void i_click_the_button() {
        TestRunner.ddHome.button.click();
    }
    @Then("I should see an alert with some text")
    public void i_should_see_an_alert_with_some_text() {
        TestRunner.wait.until(ExpectedConditions.alertIsPresent());
        Assert.assertEquals("this shows up after 3 seconds!",TestRunner.driver.switchTo().alert().getText());
    }
    @Then("I should no longer see the button")
    public void i_should_no_longer_see_the_button() {
        TestRunner.driver.switchTo().alert().accept();
        TestRunner.wait.until(ExpectedConditions.invisibilityOf(TestRunner.ddHome.button));
    }

}
