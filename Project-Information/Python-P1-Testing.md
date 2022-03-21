# Project 1

## Description
You are tasked with creating an expense reimbursement system for a small company/group. This program will allow employees to create reimbursement requests for their business expenditures, while also providing a way to track the ammount of money they have spent.
## Purpose
We want to see that you are building on the skills you have already learned, and that your understanding of the development and testing processes are solid. We also want to see that your testing abilities are expanding.

### key features
- Employee
    - should be able to log in and out of the application
    - should be able to submit reimbursement requests with a reason
        - requests should have an associated category they fall under (no less than 5 possible categories)
    - should be able to cancel a reimbursement request
    - should be able to see the total ammount of money they have requested
### Business Rules
- Employees reimburesment requests must be between $1 and $1000 per request
- Employee reimburesment request comments must be no longer than 100 characters
- Employee reimbursement requests must be in numeric form
- Employees must be given a visual notice upon a successful or failed reimbursement request

### Requirements
- Your work should follow Behavior Driven Development practices
- Your work should follow Test Driven Development practices
- You must produce and utilize the following documentation:
    - Test Strategy
    - Test Plan
    - Test Suite
    - Test Results
    - Requirement Traceability Matrix
    - User Stories
    - Acceptance Criteria
- Your data should be stored in a Postgres database
- Functionality should reflect your user stories.
- Your application should be a 3 tiered web application
- Your application should use the Data Access Object design pattern
- All requests to the application and their results should be logged in a central file.

### Testing Requirements
- All Data Access Layer methods must meet the following testing requirements:
    - they must have one positive test
    - tests must be unit tests if possible
- All Service Layer methods must meet the following testing requirements:
    - applicable methods must have one positive test
    - all business logic must have negative tests
    - tests must be unit tests if possible
    - Mocking and stubbing should be included in your testing
- All API methods must meet the following testing requirements:
    - they must all have a positive test on postman
    - they must all have a negative test for each way the request can fail on postman
- Your application should meet the following integration test requirements:
    - every user story should have an End to End test
    - every feature should have its own feature file
        - these feature files should contain both the happy path and alternative path acceptance criteria
- Each Week you must update the following testing documentation:
    - Defect report
        - what bugs are present?
        - what is their priority?
        - what is their severity?
    - Test Results
        - Pytest results
        - Postman results
        - Behave results

### Key Notes
- you do NOT have to allow for the creation of employees
    - You can have these already in the database.
- You do not need to encrypt user passwords
    - you may assume a security team will come in after your work is done to implement security measures
- Web page templates are allowed, but aesthetics are not a priority in this project.