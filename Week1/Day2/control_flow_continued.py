"""We are continuing to look at control flow in this module"""

"""
So we have already taken a look at basic control-flow using if and else statements. We know if the results of an if
statement returns a boolean true then the code block associated with that if statement will run. If it returns a 
false, then the code block will not run. If there is an else statement that code block will run if the if statement
returns a false boolean
"""

"""
As a reminder:

= is the assignment operator, it will make your variable equal to the value on the right side of the = sign

== is the comparison operator, it will return true if the values on both sides of the operator equal each other, or
it will return false if they do not equal each other
"""

my_variable = True

if True:
    print("This code block will run")
else:
    print("This code block only runs if the if statement returns a false boolean")

if 5 + 5 == 11:
    print("this phrase will never print because 5 + 5 always equals 10, not 11")
else:
    print("This phrase is going to print because 5 + 5 == 10, and so the if statement will always return false")

"""
Sometimes it is helpful to find situations where things DO NOT equal one another. In these cases, our logical true
is actually going to be produced when things are not equal. To check if things are not equal, we can use the not equal
operator, which is !=
"""

if 5 + 5 != 11:
    print("despite the two values not equaling one another, this code block is still going to run")
else:
    print("5 + 5 does not equal 11, so the if statement is getting a true boolean back, so this else will not run")

"""
the two if statements below are both going to run their block of code, but this is not always desireable. Sometimes
you want your code to ONLY run if a specific instance is true, not multiple instances. To have greater fine-tune
control over your code flow you can make use of elif statements
"""

if 5 + 5 == 10:
    print("this statement will print")
if 6 + 6 == 12:
    print("this statement will also print")

if 5 + 5 != 11:
    print("This is a true statement")
elif 6 + 6 == 12:
    print("This is also a true statement, but because the previous if returned a true boolean, this code block will never run")

"""
Here is an example of when we could use the elif statement: we are checking if a username meets our arbitrary
requirements. In this case, it is a bit too long, so the user is going to be informed that their username is too
long
"""

username = "MyFav0riteUsername"
# usernames should be no longer than 10 characters long, and no shorter than 5

if len(username) < 5:
    print("Bad username! It must be no shorter than 5 characters!")
elif len(username) > 10: # if username is bad, print bad username statement
    print("Bad username! It must be no longer than 10 characters")
else:
    print("Your username is good to go!")

"""
You don't just have to use the == and != operators, Python also supports using the keywords "is" and "is not". The
key difference between the equality operator (==) and the "is" keyword is that the equality operator is checking
values, whereas the "is" keyword is checking memory location.
"""

if 5 + 5 == 10: # The equality operator is checking to see if the value of the two statements are equal
    print("this is a true statement")

if 5 + float(5) is 10: # the "is" keyword is checking to see if both statements reside in the same computer memory space
    print("because the first five is an int and the second is a float, their value will be converted to a float, so"
          "it will actually reside in a different spot of memory, despite them both being 10 in value")

