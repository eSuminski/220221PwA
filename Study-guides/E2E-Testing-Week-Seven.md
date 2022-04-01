## Behavior Driven Development
- Development from the User perspective
    - Unlike TDD, BDD focuses on what the user is doing
    - BDD takes into account the user experience, user expectations, etc.
    - BDD takes into account ALL of your application
        - User experience
        - API you are using
        - Server you are using
        - Database you are connecting to
- End to End testing (E2E)
    - E2E tests simulate what the user would do with your frontend
        - logging in to a website
        - creating an account
        - submitting information
    - It can also simulate other activities
        - browsing the web
        - running snippets of code
        - videogames (if you can get your app to speak to the game itself...)
        - etc.

## User Stories
- These are the different actions a user can take with your application
    - These follow a predetermined syntax:
        - As a... (who is doing the action?)
            - customer
            - manager
            - owner
            - visitor
            - etc.
        - I want to... (what are they doing?)
            - login
            - logout
            - order food
            - cancel an order
            - browse a catalog of items
            - etc.
        - So that... (what is the goal?)
            - I can access my account
            - I can eat
            - I can fix a mistake I made on my purchase
            - I can look for things I might want to buy
            - etc.
    - User Stories should be as explicit and specific as you can make them
- Benefits of creating User Stories:
    - It outlines your application for you
        - Each User Story tells you some functionality you will need to code into your applicatino
    - it provides guardrails for your application
        - feature creep is a problem: you don't want to create features that are irrelevant to your project
        - User Stories help guide you on determining what is appropriate and not appropriate for your application

## Gherkin
- The syntax used in BDD to write Acceptance Criteria for the User Stories
    - Feature: high level description of a User Story or group of User Stories
    - Scenario: explicit or direct description of a User Story
    - Given: starting point for implementing the Acceptance Criteria
    - When: action needed to complete Acceptance Criteria
    - Then: ending point for Acceptance Criteria
- There are a few other key words to be aware of:
    - Scenario Outline: same as scenario, but it allows you to inject multiple different parameters into your Acceptance Criteria steps
    - Examples: parameters for the Scenario Outline are listed here

## Acceptance Criteria
- Step-by-step instructions for achieving your User Stories from the perspective of the user
- Utilizes **Gherkin** syntax
- **Feature**: Customers should be able to access their accounts
    - **Scenario**: As a customer, I want to login so I can access my account
        - **Given**: I am on the login page
        - **When**: I enter my username
        - **When**: I enter my password
        - **Then**: I should be logged in and sent to the user homepage
    - **Scenario outline**: As a customer, I want to browse the catalog of items so I can decide what to buy
        - **Given**: I am on the catalog page
        - **When**: I enter "\<item\>" into the search bar
        - **When**: I click the search button
        - **Then**: I should see the listing for "\<item\>"
    - **Examples**:
        - | item |
        - | apple |
        - | shoes |
        - | goat |

## Behave
- Testing framework that supports End-to-End testing (E2E)
- Can take Acceptance Criteria and generate code steps for implementing them
    - Create feature file (filename.feature)
    - Use Gherkin syntax to write out your Acceptance Criteria in the feature file
        - You should already have Acceptance Criteria written out for your User Stories
    - Run feature file: it will fail, but it will also generate methods for each Given, When, and Then statement that is not yet implemented (will need to install plugin for cucumber to make this work, Gherkin as well)
        - Can also utilize tidy Gherkin on Google to auto-generate code stubs 
    - Write code to implement the Acceptance Criteria steps

## Selenium
- Browser automation software
    - NOT A TESTING SOFTWARE
        - It is very useful for testing purposes, but it is not explicitly designed for testing
- If Cucumber is peanutbutter, Selenium is choclate: they are not the same, but they work incredibly well together
- Selenium can automatically get and interact with webpages, you simply have to tell it where to go and what to do
    - This is accomplished by utilizing web drivers
        - different browsers (chrome, edge, firefox, etc.) have their own web drivers you can download
        - Selenium utilizes these drivers to interact with web pages via the chosen web browser

## End to End Test
- Test that ensures your application achieves all your Acceptance Critieria
- Simulates the actions a user would take with your application
- Is much faster at checking the functionality of your front end than manual testing
    - This is seen more clearly in larger applications

## Shorthand BDD Steps
- Step 1: You have to set up your User Stories
- Step 2: Create Acceptance Criteria for your User Stories
    - Step 2.1: Create a visual that maps out the steps taken in your Acceptance Criteria
- Step 3: Create application
    - Utilize TDD to design app
- Step 4: Create feature files for E2E tests
    - Step 4.1: Generate methods for Acceptance Criteria
- Step 5: Create runner class to run your feature files
- Step 6: Create Page Object Models (poms) for required pages
    - Don't forget to update your runner as you add more poms
- Step 7: Create Step classes to implement your generated code stubs for your Acceptance Criteria 
- Step 8: Run your automated E2E tests!

## E2E example
See Week6 Day4 file for examples of complete E2E tests