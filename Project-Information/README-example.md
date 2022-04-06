<!-- Example Readme MD -->

# ERS--Python
## My reimbursement application for Viridian Dynamics
This application was designed for Viridian Dynamics employees to be able to submit reimbursement requests for their expenditures. Once their requests are submitted the managers may log in and either approve or deny the request.

## Technologies Used
- JavaScript 
- HTML
- CSS 
- SQL 
- Python 
- Flask 
- Postman 
- Selenium 
- AWS RDS
- REST 
- Flask 
- Cucumber 
- Git

## Features
- Employees can submit reimbursement requests.
- Employees can view previous reimbursement requests.
- Managers can view reimbursement requests.
- Managers can approve reimbursement requests.
- Managers can deny reimbursement requests.
- Managers can view statistics about employee reimbursements.

**to do**
- update webpages to have uniform color/appearances.
- create dynamic charts that represent the statistics currently shown in just numeric values.
- add an easy to use method to close the application

## Getting Started
- to clone:
  -  git clone https://github.com/eSuminski/ERS--Python.git
- Database:
  -  Create a local or cloud based Postgres RDS
  -  Use your prefered database management software to run Script-7.sql to set up the database
- to deploy:
  - install the application requirements found in the requirements.txt file, preferably in a virtual environment
  - navigate to the Pythoncode file in your chosen terminal
  - py -m pip install -r requirements.txt  
  - use the command py main.py to start the application(currently no in-app way to end the application)

## Usage
- Employees can log into the reimbursement portal to manage their reimbursement requests:
  - Employees can make reimbursement requests
  - Employees can give a reason for their reimbursement requests
  - Employees can view the status of their reimbursement request
- Managers can log into the reimbursement portal to manage employee reimbursement requests:
  - Managers can approve or deny requests using the status code key provided within the portal
  - Managers can view statistics 