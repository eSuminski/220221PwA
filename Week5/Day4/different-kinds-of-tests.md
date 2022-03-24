# Different kinds of tests

### Functional Testing
You are already familiar with this kind of test: given the correct input, do you get back the expected output? This kind of test is not interested in optimization: it is only concerned with functionality.

### System Testing
If unit testing is checking functionality, think of System testing as a functional test for your entire application. I our case, we will be using End to End testing to do our System Testing. It is common for System Testing to happen when Behavior Driven Development practices are being followed, and the user perspective is commonly the starting point for any System Test. 

### User Acceptance Testing
UAT is about testing the user-friendliness of your application: it aims to answer questions like:
- Is the application intuitive for the user?
- Is the application pleasant to look at?
- Is the app responsive to user commands?
- How hard do I need to think to use the application?

At this time, no one knows how to automate UAT, and so this kind of test needs to be handled manually. Usually when UAT is done there are two levels of testing that happen: Alpha and Beta testing. 
- Alpha testing is where the developers do the UAT
- Beta testing is when you have a select group of end users perform UAT

### Performance Testing
If functional testing is about checking whether your application works as intended, performance testing is about checking the optimization of your application. These can be tests checking how long it takes to perform a function, how much memory is used, how much processing power is used, etc.

### Stress Testing
Stress testing is about testing the application in unusual scenarios:
- what happens if 100 people try and choose the same username at the same time?
- what if 10,000 people try and log in at the same time?
- what if 500 people try to buy the same 4 items?

### Load Testing
Load testing is about testing how well your application handles multiple users at once. This is figuring out things like the maximum number of users your application can handle before it starts to break. It is also common to use load testing to figure out the optimal amount of users. This is a useful way to figue out what the expected heavy, medium, and light levels of traffic are that you should aim for.

### Spike Testing
Most modern applications perform auto-scaling, which is a service provided by most cloud computing providers (think Amazon, Microsoft, Google). Spike testing is used to make sure that your application scales up and down appropriately.

### White Box Testing
White box testing is writing tests for code you have access to
### Black Box Testing
Black box testing is writing tests for code you don't have access to