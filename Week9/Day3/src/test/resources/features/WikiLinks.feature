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