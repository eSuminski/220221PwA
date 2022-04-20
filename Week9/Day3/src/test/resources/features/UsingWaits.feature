Feature: I should be able to interact with elements using waits
  Scenario: As a user I should be able to use waits to interact with elements and check that elements have disappeared
    Given I am on the delay-disappear page
    When  I click the button
    Then  I should see an alert with some text
    Then  I should no longer see the button