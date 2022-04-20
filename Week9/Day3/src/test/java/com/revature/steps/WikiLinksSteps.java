package com.revature.steps;

import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;

public class WikiLinksSteps {

    @Given("I am on the Wikipedia home page")
    public void i_am_on_the_wikipedia_home_page() {
        // this step, despite being used in multiple feature files, only needs to be defined once
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
