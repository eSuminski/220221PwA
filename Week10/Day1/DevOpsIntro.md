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