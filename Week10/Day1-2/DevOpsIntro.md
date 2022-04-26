# DevOps
Software Development and Operations (DevOps) is a methodology that combines the development, deployment, and maintenence of code into a single, streamlined process. Ideally, this process is automated as much as possible (though full automation is not always possible). There are five general steps to the DevOps process:
1. Source Code Control
    - you are already familiar with this step: this is the creation of code (following TDD and BDD practices) and publish that code to a central repository.
2. Building and Testing
    - You would normally be testing all along the way, but this step is the final, overarching test and build step. This is the round of testing that you want to make sure you generate reports off of that can be shared with clients and/or other developers.
3. Deploying to Staging
    - the staging environment (or testing environment, the non-production environment) is where you can test the entirety of your application without it affecting your production environment
4. Acceptance Testing
    - this is where you run your E2E tests, any other integration tests you need to run, your user acceptance testing, etc. 
5. Deployment of Build
    - this is the actual deployment of your application

## DevOps & Agile
There are three common practices for implementing DevOps while doing Agile development. These practices are called Continuous Integration, Continuous Delivery, and Continuous Deployment (CI, CD, CD).
- Continuous Integration
    - This is the practice of regularly and consistently merging code into a central repository. It usually will also include the revewing of code to ensure that integration is as smooth as possible.
- Continuous Delivery
    - CD is the practice of automating the DevOps pipeline as much as you can WITHOUT automating the entire process. This means that once your code is merged into the central repository it is downloaded and built/tested in a staging environment. This means we can easily automate steps 1-3 of the Devops process, and it is also possible to automate step 4 (though this is generally harder to do). With this practice the depkoyment off the production build should be done manually, since the automated tests and manual Acceptance testing may reveal bugs
- Continuous Deployment
    - CD is the all-encompasing Agile practice of DevOps: it is the practice of automating EVERY step of the DevOps methodology. When it works, it is incredible: you save a ton of time on mundane processes, and it allows you as developers to focus on what you do best: develope your application. However, this does require many guard-rails be instituted in order to make sure the full automation of the pipeline does not lead to a broken application in the production environment