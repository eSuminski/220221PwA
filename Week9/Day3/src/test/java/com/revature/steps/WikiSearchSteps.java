package com.revature.steps;

import com.revature.runner.TestRunner;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;

public class WikiSearchSteps {

    @When("I enter {string} into the search bar")
    public void i_enter_into_the_search_bar(String string) {
        TestRunner.wikiHome.sendKeysToSearchbar(string);
    }
    @When("I click the search button")
    public void i_click_the_search_button() {
        TestRunner.wikiHome.clickSearchButton();
    }
    @Then("I should be redirected to the {string} page")
    public void i_should_be_redirected_to_the_page(String string) {
        Assert.assertEquals(string, TestRunner.driver.getTitle());
    }
}
