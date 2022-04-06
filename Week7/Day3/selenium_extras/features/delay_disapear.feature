Feature: I can wait for elements to appear and check elements have been removed
  Scenario: I can wait for elements, and check they have disappeared
    Given I am on the homepage
    When  I click the button
    Then  I should be able to read an alert with some text in it
    Then  I should no longer be able to see the button