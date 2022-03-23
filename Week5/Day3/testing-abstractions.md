# Testing Abstractions

### Testing Mindset
Having a testing mindset is something that you develop overtime. Writing a test to make sure the functinality is working as intended is easy: knowing EVERYTHING that could potentially go wrong and testing for it is far more difficult, and as you learn more about your application, systems you are using, and the peculiarities of the language you are writting with, you will find more comprehensive ways to write tests. This is not an arbitrary requirement companies give their testers: the more efficient your tests are, the greater scalability your app will have. The more comprehensive your tests are the easier it is to answer: "can we make our app do {thing}?" The more comprehensive your tests are the easier it is to immediately know what is and is not possible. There are a few basic testing concepts to keep in mind as you start your testing career:
1. Positive Tests
    - how does the function handle correct input?
2. Negative Tests
    - how does the function handle incorrect input?
        - right type wrong data
        - wrong type
        - etc.
3. Edge cases
    - how does the function handle weird cases or extreme values?
        - how does it handle 0?
        - how does it handle an empty string?
        - how does it handle a really large number/string?
        - how does it handle an sql statement passed as an argument?
        - how does it handle losing connection to the database it is supposed to retrieve data from?
        - etc.
4. Redundancy
    - are your tests actually telling you something new?
        - passing in strings that are 6, 7, 8, 9, and 10 characters long into a function that takes a max of 5 characters doesn't tell you anything new
        - testing for your function to throw a divide by zero error when you divide by zero is redundant

### Pyramid Testing
There are three general levels of testing you can classify your tests into: unit, integration, and end to end. You can view it like a pyramid, with Unit tests supporting integration, and integration supporting e2e. What this means is that the majority of your tests should be unit tests. Every piece of functionality should have a unit test if possible, and these unit tests should test the intended, unintended, and edge cases. Integrated tests are the next level of the pyramid, which should still be extensive, but by its nature it will not have as many tests as the Unit tests. Finally, End to end tests are at the top of the pyramid and are the least frequent. These can work once your unit tests and integration tests are complete, and you can focus on testing the front end and back end together.

### Standard Development Life Cycle
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

### Standard Testing Life Cycle overview
The testing lifecycle is very similar to the SDLC; you can think of the STLC as a subset of the SDLC: They are not the same thing, but the pattern they follow is similar. The STLC is used when a piece of software has already been developed and it now needs to be maintained.
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
    - etc.
4. Set up test environment
    - create test server
    - create database with dummy data
    - create mock API endpoints
5. Run tests
    - generate test report
    - report new bugs

### Feature vs Defect
We all know what a feature is: it is some kind of functionality in our application. A defect (or bug) can sometimes be a little trickier to determine. This is because there are just SO MANY WAYS an application can surprise you. You may write your tests, have them all pass, but then users report that their experience is nothing like what you expected it to be. Then there is the "it's not a bug: it's a feature" moments when something unexpected ends up staying in the code because you like what it does to or for the app. Because of this, there is a general defect lifecylce you should follow to determine whether an unexpected instance is truly a defect or a surprise feature
### Defect lifecycle
1. A bug is reported (could be from a test, user reported, etc)
2. the bug is assigned to a person or team
3. The bug is analyzed and/or recreated
    - the bug will either be rejected or deemed worth addressing
    - it could be rejected because the bug could not be reproduced, it is deemed a feature instead of a bug, an upcoming updated will fix the problem, etc
    - in this case, the bug status will be closed/finished, and you move on
4. assuming the bug needs to be addressed/fixed, you work on the code and test it thoroughly
    - if you/ your team can not fix the bug you report it and the bug is reassigned
5. Once the bug is fixed you close the bug status and move on
### Defect Reports
Defect reports are simply how you report a bug. These can be incredibly basic (a text file that list the bugs needing to be fixed) or they can be incredibly complex (including defect id, project and product, release version, summary, descriptions, steps to replicate, expected vs actual results, comments, the list goes on). The means of reporting a defect and the expectations for how it should be done should be available either within the test strategy or test plan documentation. While working on your projects in training you should have a consistent way of reporting problems with your application to your teammates so that everyone is on the same page. It does not need to be fancy or all inclusive, but it should be consistent.
### Severity vs Priority
Severity and Priority are two different metrics for determining how much a defect affects your product. Severity is a measurement of how much the defect affects one or more features, while priority measures how quickly the defect ought to be addressed. Usually the two go hand-in-hand (high priority == high severity) but this is not always the case.
- high priority low severity
    - your company landing page has a competitors' logo in place of your own
    - functionally, this does not affect your website. That being said, promoting your economic cometitor on your home page is not a great buisness move, so it should be fixed ASAP
- low priority high severity
    - your apps function to change names in the company database has completely broken
    - this would be annoying for those who are trying to fix or change their names in the database, but it does not break the ability for the app to do its intended job, so fixing something like the wrong logo on the landing page would be higher priority to fix first
### logging defects
If defect reports are a way of managing bugs as they arrise, logging defects is a way of recording them for posterity. Again, the means of handling defect logging should be available to you in the test strategy/plan documentation, but for your own projects you will want to create a system of codifying and logging the bugs your application runs into. This can be useful for tracking any persistent bugs: knowing that your login system constantly bugs out may indicate you need to rework it from the ground up. Having the log is a good means of determining if such a drastic measure is warranted.