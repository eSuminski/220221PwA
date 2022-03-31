Feature: Users who read different languages should be able to browse Wikipedia in their own language

  Scenario: As an English reader, I want to browse Wikipedia in English so I can understand what I am reading
    Given I am on the Wikipedia home page
    When  I click on the English link
    Then  I should be on the English Wikipedia main page

  Scenario: As a Spanish reader, I want to browse Wikipedia in Spanish so I can understand what I am reading
    Given I am on the Wikipedia home page
    When  I click on the Spanish link
    Then  I should be on the Spanish Wikipedia main page

  Scenario: As an Italian reader, I want to browse Wikipedia in Italian so I can understand what I am reading
    Given I am on the Wikipedia home page
    When  i click on the Italian link
    Then  I should be on the Italian Wikipedia main page