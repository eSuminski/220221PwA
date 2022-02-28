# Banking Application

## Description
Your job is to create a simple banking app that allows the following:
- users can join the bank
- users can create a bank account
- users can deposit and withdraw money
- users can view their accounts individually or collectively
- users can close their accounts
- users can leave the bank
	
## Purpose

We want to see that you can meet deadlines, that you can code, and that you have a firm grasp of testing basics. You are expected to complete the following requirements and give a 5 minute presentation of your project to our QC team.

## Requirements
1. Functionality should reflect the provided user stories.
2. Data should be stored in a database
3. Your application should be a 3 tiered web application
4. Your application should use the Data Access Object design pattern
5. All requests to the application should be facilitated through Postman and handled by Flask.
6. All requests to the application and their results should be logged in a central file.
7. Test Driven Development should be used to create your application

## User Stories (suggested method name)

* As a customer, I can start a business relationship with the bank so I can store my money securely(create_customer)
* As a customer, I can create a new bank account with a starting balance so I have somewhere to store my money (create_account)
* As a customer, I can view the balance of a specific account so I can check my finances (get_account_by_id)
* as a customer, I can view the balance of all my accounts so I know exactly how much money I have (get_all_accounts_for_user)
* As a customer, I can make a withdrawal from a specific account so I can have access to my money (withdraw_from_account_by_id)
* As a customer, I can make a deposit to a specific account so I can store my money for safe keeping (deposit_into_account_by_id)
* As a customer, I can transfer money between accounts so I can consolidate my money (transfer_money_between_accounts_by_their_ids)
* As a customer, I can close any of my bank accounts so that it is easier to remember where my money resides (delete_account_by_id)
* As a customer, I can end my relationship with the bank when it is no longer needed (delete_customer_by_id)

## Business Rules

- Bank accounts may not have a negative value
- Bank accounts must work with numbers
- Bank accounts must have unique Ids
- Customer first and last names may not exceed 20 characters
- Customers must have unique Ids

## Testing Requirements
- All Data Access Layer methods must meet the following testing requirements:
    - they must have one positive test
    - they must have at least one negative test
        - you should try and test for every way your method can fail
- All Service Layer methods must meet the following testing requirements:
    - applicable methods must have one positive test
    - all business logic must have negative tests
- All API methods must meet the following testing requirements:
    - they must all have a positive test on postman
    - they must all have a negative test for each way the request can fail on postman