Feature: As a user I should be able to search for different articles on Wikipedia
  Scenario Outline: As a user I should be able to search different things on Wikipedia
    Given I am on the Wikipedia home page
    When  I enter "<value>" into the search bar
    When  I click the search button
    Then  I should be redirected to the "<title>" page
    Examples:
      | value | title |
    | puppy | Puppy - Wikipedia|
    | apple | Apple - Wikipedia|