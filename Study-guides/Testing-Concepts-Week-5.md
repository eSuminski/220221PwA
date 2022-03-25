## Pyramid Testing
There are three general levels of testing you can classify your tests into: unit, integration, and end to end. You can view it like a pyramid, with Unit tests supporting integration, and integration supporting e2e. What this means is that the majority of your tests should be unit tests. Every piece of functionality should have a unit test if possible, and these unit tests should test the intended, unintended, and edge cases. Integrated tests are the next level of the pyramid, which should still be extensive, but by its nature it will not have as many tests as the Unit tests. Finally, End to end tests are at the top of the pyramid and are the least frequent. These can work once your unit tests and integration tests are complete, and you can focus on testing the front end.
## Testing Mindset
Having a testing mindset is something that you develop overtime. Writing a test to make sure the functinality is working as intended is easy: knowing EVERYTHING that could potentially go wrong and testing for it is far more difficult, and as you learn more about your application, systems you are using, and the peculiarities of the language you are writting with, you will find more comprehensive ways to write tests. This is not an arbitrary requirement companies give their testers: the more efficient your tests are, the greater scalability your app will have. The more comprehensive your tests are the easier it is to answer: "can we make our app do {thing}?" The more comprehensive your tests are the easier it is to immediately know what is and is not possible. There are a few basic testing concepts to keep in mind as you start your testing career:
1. Positive Tests
    - how does the function handle correct input?
2. Negative Tests
    - how does the function handle incorrect input?
        - right type wrong data
        - wrong type
3. Edge cases
    - how does the function handle weird cases or extreme values?
        - how does it handle 0?
        - how does it handle an empty string?
        - how does it handle a really large number/string?
        - how does it handle an sql statement passed as an argument?
4. Redundancy
    - are your tests actually telling you something new?
        - passing in strings that are 6, 7, 8, 9, and 10 characters long into a function that takes a max of 5 characters doesn't tell you anything new
        - testing for your function to throw a divide by zero error when you divide by zero is redundant
## Testing Lifecycle
The testing lifecycle is very similar to the SDLC; you can thik of the STLC as a subset of the SDLC.
1. Requirement Analysis
    - what user stories need testing?
2. Create Test Plan
    - What is the workflow for writing tests?
    - how will the testing team be organized?
    - how will our results be stored?
    - what technologies will we use for our testing?
3. Design test cases
    - what are our unit tests?
    - what are our integration tests?
    - what are our End to End tests?
    - what are our positive tests?
    - what are our negative tests?
4. Set up test environment
    - create test server
    - create database with dummy data
    - create mock API endpoints
5. Run tests
    - generate test report
    - report new bugs
## Testing Types
There are more kinds of tests than just the unit/integration tests:

Functional Testing
- These are tests that make sure a function is working
- it is very basic: given the right input, does this function do what I want it to do?
- optimization is irrelevant to this test: you just need to know if the test works or not

System testing (End to End testing)
- These are tests that check the entirety of an application
- do the front end and back end work together as intended?
- These are often run from the user experience: will I be logged in correctly if I enter my login credentials?

UAT (User Acceptance Testing)
- These are tests to determine the user-friendliness of your application
    - very subjective, must be done manually
    - is the app intuitive?
    - is it pleasant to look at?
    - is the app responsive?
    - how hard do I need to think to use the app?
    - can involve alpha and beta testing
        - Alpha testing is when developers do the UAT
        - Beta testing is when end users test the application
            - what is intuitive to the developer may not be to the end user

Performance Testing
- These tests help determine the efficiency of your application
    - These tests can check the time, memory, or processing efficiency of the application
- Load Testing
    - tests how well the application can handle multiple users
        - can test expected traffic, heavy traffic, light traffic, etc.
        - is common to load traffic until app breaks to find the limit of the app
- Stress Testing
    - tests the application in unusual scenarios
        - what if 100 people try and choose the same username at the same time?
        - what if 10,000 people login at the same time?
        - what if 500 people try to buy the same 5 items at once?
- Endurance testing
    - These are the same as load test, but over a longer period of time
        - these tests are for finding those errors that take a long time to discover
            - what happens if a log file gets too large?
            - is there a memory leak?
- Spike test
    - these tests help determine how well (or how poorly) your application can scale
        - most modern apps perform auto-scaling, so the number of server handling requests increase or decrease depending on the traffic
## Testing Documents
There are a few general testing documents you should be familiar with, though their implimentation may change from company to company

Test strategy
- This is a high level document: it is applicable company-wide
- includes information on how to report bugs and make test reports
    - API endpoint documentation rules
    - workflow for bug fixes
    - etc
- includes roles and responsibilities

Test plan
- this is a document that is specific to a particular project
    - contains information on the technologies used in the project
    - contains dealine schedules, important dates
    - documents what is actually being tested
        - also notes what is NOT being tested

Test cases
- these are singular tests (the actual test itself)

Test results
- these are collections of tests (test cases) that are related to each other (employee entity tests, employee route tests, etc)

## Requirements Traceablity Matrix
This is a document that provides detailed information about what is being tested, how it was tested, its testing status, and who is doing the testing.
![requirements traceability matrix](requirement_traceability_matrix_example.png)

## pytest data provider
Pytest does not have an easy to access reporting option, but there are packages you can download to generate reports from your tests. The one we will use is pytest-html
```cli
pip install pytest

pip install pytest-html
```
Once you have done this you can run your pytests like normal, and all you need to change to generate the report is add commands to the end of the command
1. to generate your basic reports just add --html=report.html to the end of the command
```cli
pytest test_pacakage --html=report.html
```
this will generate the report for you, but it will create separate folder for any images and styling that are applied to the report. 
2. Instead of this, you can alter the command slightly to make the report self contained
```cli
pytest test_pacakge --html=report.html --self-contained-html
```
this will generate the html report without creating the extra files to contain the css and images. It is an easier report to share with others.
## SDLC overview
The SDLC is the workflow for creating a piece of software. There is no "official" or perfect SDLC, and different organizations will have their own take on the SDLC. All of them will have a similar structure as outlined below, or at least include them somewhere in their development lifecycle:
1. Determine Software Requirements
    - this is the first step of developing a piece of software: you need to know/decide what it needs to do
        - does it need to be fast above all else? Easy to use above all else? Look good, even if it does not work? etc.
    - User stories are developed at this time
2. Design the software
    - interfaces are created at this point
    - determine front end technology (angular? plain html/css/js?)
    - determine back end technology (server language? endpoints? entities? services?)
3. develop/test
    - create tests and write code to pass tests
4. deploy
    - software packaging happens at this point
        - web app deployed to AWS, executable jar file created, etc.
5. monitor/perform maintanance
    - keep track of the application while it is use
        - monitor traffic, review logs, keep track of client comments, investigate bugs, etc
## STLC overview
The testing lifecycle is very similar to the SDLC; you can thik of the STLC as a subset of the SDLC.
1. Requirement Analysis
    - what user stories need testing?
2. Create Test Plan
    - What is the workflow for writing tests?
    - how will the testing team be organized?
    - how will our results be stored?
    - what technologies will we use for our testing?
3. Design test cases
    - what are our unit tests?
    - what are our integration tests?
    - what are our End to End tests?
    - what are our positive tests?
    - what are our negative tests?
4. Set up test environment
    - create test server
    - create database with dummy data
    - create mock API endpoints
5. Run tests
    - generate test report
    - report new bugs
## Quality Assurance vs Quality Control
These two topics both drive towards the same goal: a high level of functionality, efficiency, and good structure in an application. The difference between the two is that Assurance is a mindset that must be determined before the project is started, and Control is a reactive process that refines the application
- Quality Assurance
    - this is a proactive philosophy
        - How are we going to design the application in a way that includes quality gates and standards?
            - what are our coding standards?
                - Python methods must be type annotated
            - what are our testing standards?
                - every method must have a positive, negative, and at least two edge case tests
            - what are our documentation standards?
                - all modules, classes, and methods must have a docstring
            - what are our development standards?
                - all github merges must be approved by a senior developer
- Quality Control
    - this is a reactive process
        - are there bugs that need to be fixed?
        - do reports need to be revamped?
        - do any methods need to be updated
        - have all features been added to the automated reports?
        - is a server down that needs to be rebooted?
## Feature vs Defect
We all know what a feature is: it is some kind of functionality in our application. A defect (or bug) can sometimes be a little trickier to determine. This is because there are just SO MANY WAYS an application can surprise you. You may write your tests, have them all pass, but then users report that their experience is nothing like what you expected it to be. Then there is the "it's not a bug: it's a feature" moments when something unexpected ends up staying in the code because you like what it does to or for the app. Because of this, there is a general defect lifecylce you should follow to determine whether an unexpected instance is truly a defect or a surprise feature
## Defect lifecycle
1. A bug is reported (could be from a test, user reported, etc)
2. the bug is assigned to a person or team
3. The bug is analyzed and/or recreated
    - the bug will either be rejected or deemed worth addressing
    - it could be rejected because the bug could not be reproduced, it is deemed a feature instead of a bug, an upcoming updated will fix the problem, etc
    - in this case, the bug status will be closed/finished, and you move on
4. assuming the bug needs to be addressed/fixed, you work on the code and test it thoroughly
    - if you/ your team can not fix the bug you report it and the bug is reassigned
5. Once the bug is fixed you close the bug status and move on
## Defect Reports
Defect reports are simply how you report a bug. These can be incredibly basic (a text file that list the bugs needing to be fixed) or they can be incredibly complex (including defect id, project and product, release version, summary, descriptions, steps to replicate, expected vs actual results, comments, the list goes on). The means of reporting a defect and the expectations for how it should be done should be available either within the test strategy or test plan documentation. While working on your projects in training you should have a consistent way of reporting problems with your application to your teammates so that everyone is on the same page. It does not need to be fancy or all inclusive, but it should be consistent.
## Severity vs Priority
Severity and Priority are two different metrics for determining how much a defect affects your product. Severity is a measurement of how much the defect affects one or more features, while priority measures how quickly the defect ought to be addressed. Usually the two go hand-in-hand (high priority == high severity) but this is not always the case.
- high priority low severity
    - your company landing page has a competitors' logo in place of your own
    - functionally, this does not affect your website. That being said, promoting your economic cometitor on your home page is not a great buisness move, so it should be fixed ASAP
- low priority high severity
    - your apps function to change names in the company database has completely broken
    - this would be annoying for those who are trying to fix or change their names in the database, but it does not break the ability for the app to do its intended job, so fixing something like the wrong logo on the landing page would be higher priority to fix first
## logging defects
If defect reports are a way of managing bugs as they arrise, logging defects is a way of recording them for posterity. Again, the means of handling defect logging should be available to you in the test strategy/plan documentation, but for your own projects you will want to create a system of codifying and logging the bugs your application runs into. This can be useful for tracking any persistent bugs: knowing that your login system constantly bugs out may indicate you need to rework it from the ground up. Having the log is a good means of determining if such a drastic measure is warranted.

## Positive vs Negative Tests
Positive tests are those that check to see if your functions work as intended. If they receive the correct data, the correct response should be returned. Negative tests check to see if your function can handle things going wrong. This could be the wrong data being provided to your function, type discrepancies (wrong data type being passed as an argument, some sort of exception being raised), there are so many ways things can go wrong. Negative tests check to see if your functions can handle these situations

## Data Driven Testing
Data Driven testing is a form of testing where the test data is stored in some form of spreadsheet, both the inputs and the outputs. The advantage of this is that all the test data is available in a single location: you can see what data is going into the tests, and what material is being returned from the test. By seperating the the test data from the functions performing the tests you make it easier to reuse tests in different parts of your application. Where this can fall apart, however, is if you have an incredibly large ammount of data and functionality to test. By design, Data Driven Testing creates a lot more paperwork than just Automated Testing. With Automated testing you only need to see the generated report, but with Data Driven testing you also need to check the inputs in your test spreadsheet. The extra paperwork also means you have more documentation to write, something that is harder to automate than with simple Automation testing.

## Behavior vs State verification
We've talked about behavior and state verification in our application, but it also applies to our project as a whole. Behavior verification should be familiar to us: you are testing to make sure your project's functionality is working as intended. State verification, on the other hand, is a test to make sure that your database has ACTUALLY changed (or not changed) as you intended. These tests are fundamentally different from behavior tests: they are not interested in whether the function works as intended or not. All they are verifying is whether the STATE of the database (or object, etc) is what we expect it to be.

## Web Service Testing
This is what we have been doing with Postman, and will do with behave and Selenium. It is validating that our http requests are being recieved, handled, and responded to properly.