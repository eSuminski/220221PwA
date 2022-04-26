# SonarCloud & SonarLint
These are code quality tools that help you find code "smells" in your application. These are things like:
- Data security issues
- Bugs
- confusing code
- redundant code
- unused imports
- empty code blocks
- etc.

Most IDEs have code quality tools built in, but these can provide more in-depth analysis of your code.
- SonarCloud
    - A cloud code analyizer that can review code loaded into a cloud-based repository, like github
        - Navigate to the Sonar Cloud Login Page, and select "Log in with Github"
        - Click on "Analyze your code" and follow the steps for project setup
        - Select the repository to analyze.
- SonarQube
    - A code review tool that can be built into a devops pipeline. Because it is more configurable it could been seen as more powerful
- SonarLint
    - an opensource plugin for many ides, it can be installed from your IDE's plugin marketplace.