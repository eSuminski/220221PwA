"""This module contains notes and examples about exceptions"""

"""
Whenever something goes wrong in your code an exception is raised. There are many built in exceptions that Python
will supply you from the get go
"""

# print(10/0) this will produce a ZeroDivisionError because you can't divide by 0

my_dictionary = {}

# print(my_dictionary["key"])this will produce a KeyError because the requested key does not exist
# print("this is after the exception is raised") if i run the code above this line will not execute

"""
We can actually write code to handle these exceptions: to do this we need to use try/except blocks
"""

try:
    print(11/1)
except ZeroDivisionError as e:
    print("Whoops! you tried to divide by zero")
    print(str(e))

"""
You can create your own custom exceptions to handle unique situations that your Python code itself
would not normally have a problem runnning. For example, strings can be longer than 10 characters, but
you may want people to not have usernames longer than 10 characters. You could create a custom exception
for situations when someone tries to create a username in your application longer than 10 characters
"""

class UsernameTooLong(Exception):
    pass

try:
    desired_username = "longer than 10 characters"
    if len(desired_username) <= 10: # if username is 10 characters or less, account is created
        print("account created")
    else: # our code will raise an exception if the username is longer than 10 characters
        raise UsernameTooLong("Please make username no longer than 10 characters")
except UsernameTooLong as e: # we add this except block to handle the UsernameTooLong Exception IF it is raised
    print(e) # we print the message associated with the exception

finally: # anything in the finally block will always run, whether or not the except block runs
    print("this will also print, whether the exception is thrown or not")

"""
Sometimes, our code has the chance to fail in more than one way: we can chain except blocks to handle all the 
possible ways that our code might fail
"""

number = 10
my_dictionary = {
    "ten":number
}

try:
    pass
    # print(my_dictionary["ten"]/0) this will make the ZeroDivisionError code block run
    # print(my_dictionary["fifty"]/0) this will make the KeyError code block run
except ZeroDivisionError as e:
    print(e)
except KeyError as e:
    print(f"The key {str(e)} does not exist inside the dictionary")
except Exception as e: # This is just to show you can do this: in a real application doing this is bad practice
    print(e)


