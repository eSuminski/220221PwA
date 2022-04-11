# Project 2

## Description
You and your team have the freedom to decide what kind of application you wish to build for your Project 2. There are a few base requirements your project must meet:
1. Your application must be able to handle at minimum two different kinds of users (customers and clerks, employees and managers, etc.)
2. Your application must persist data using an AWS Postgres database
3. Your application must be a web service
    - it must be a RESTful web service
    - use HTML/CSS/JavaScript
4. Your application should be robust
    - logging in and out is insufficient: your users must be able to DO things with your application
5. Your backend should be programmed in Java
6. Your project should be housed in a central Github repository

## Purpose
We want you to get experience working in an independent environment, setting goals, achieving them, and adjusting to change on the fly. We also want you to get experience working on a team, coordinating your work, and overcoming difficulties in a group environment.

### key features
- Your application must have at least 5 different features for each kind of user of your application
- User features should be different between the different kind of users
    - example: if making a bank app, customers should be able to withdraw and deposite funds, bankers should be able to create new accounts and close old accounts
- All users must be able to login
- All users must be able to logout


### Requirements
- You must follow the SDLC
- You must follow the STLC
- Your work should follow Behavior Driven Development practices
- Your work should follow Test Driven Development practices
- You must produce and utilize the following documentation:
    - Test Strategy
    - Test Plan
    - Test Cases
    - Test Results
    - User Stories
    - Acceptance Criteria
    - Requirements Traceability Matrix
- Your data should be stored in a Postgres database
- Functionality should reflect your user stories.
- Your application should be a 3 tiered web application
- Your application should use the Data Access Object design pattern
- Your backend should be developed using Java 8+
    - make sure all developers are using the same version
- All requests to the application and their results should be logged in a central file.

### Business Rules
You and your team must decide upon a minimum of 5 business rules your application must implement.

### Testing Requirements
- All Data Access Layer methods must meet the following testing requirements:
    - they must have one positive test
    - they must have at least one negative test
    - tests must be unit tests if possible
- All Service Layer methods must meet the following testing requirements:
    - applicable methods must have one positive test
    - all business logic must have negative tests
    - tests must be unit tests if possible
    - Mocking should be included in your testing
- All API methods must meet the following testing requirements:
    - they must all have a positive test on postman
    - they must all have a negative test for each way the request can fail on postman
- Your application should meet the following integration test requirements:
    - every user story should have an End to End test
    - every feature should have its own feature file
        - these feature files should contain both the happy path and alternative path acceptance criteria
- Each Week you must update the following testing documentation:
    - Test Results
        - TestNG results
        - Postman results
        - Cucumber results
        - Requirements Traceability Matrix