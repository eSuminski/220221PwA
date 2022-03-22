# Acceptance Criteria & Gherkin
Acceptance criteria is the step-by-step instructions for completing a user story, and they are written using Gherkin syntax

### Gherkin
Gherkin is the syntax used when doing BDD to write out the acceptance criteria for user stories. There are a few key words you should be familiar with when writting out acceptance criteria using Gherkin syntax
- Feature
    - a feature is a high level description of a user story OR a group of user stories
- Scenario
    - these are either explicitly named after the user story, or they are a detailed explanation of the user story
- Given
    - the Given keyword is used to indicate the starting situation for completing a user story
- When
    - a When keyword is used to indicate an action after the Given that must be taken to complete the user story
- Then
    - a Then keyword is used to indicate the ending point of the user story

### Acceptance Criteria Example
```gherkin
Feature: Customers should be able to log in and log out

Scenario: as a customer I want to log in to my account so I can do my shopping
    Given: I am on the login page
    When: I enter my username
    When: I enter my password
    When: I click the login button
    Then: I should be logged in and redirected to the customer home page

Scenario: as a customer I want to log out to ensure no one else uses my account
    Given: I am logged in and on the customer home page
    When: I click on the dropdown menu
    When: I click the logout button at the bottom of the menu
    Then: I should be logged out and redirected to the login page
```
### Wireframes
While your acceptance criteria determines the steps a user will take to fullfil your user stories, it can sometimes be hard to imagine those steps actually happening. For those who are more visual, wireframes can be a useful tool to visualize the acceptance critera steps.