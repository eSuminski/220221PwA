"""This module contains some basic Python notes and examples"""

"""
Python is a very popular language, one of the top used languages in the world. There are a couple features that
make it an easy language to jump into as a new developer

1. Python is a "high level" language. This means that Python will automatically handle memory management for you.
This frees you up to focus only on developing your application. This can make for faster development, but it does
mean you lose out on optimization.

2. Python is a "dynamic" language. This means that when you write your code you don't have to specify what KIND 
of data you are working with: Python will automatically assign a data type to your work. This can make for much
easier to read code, but if your naming conventions are ambiguous then it will actually make your code harder to
read

3. Python is a "strongly" typed language. This means that once a data type is set it will not be implicitly changed
by Python

4. Python is an "interpreted" language, using Just-in-Time compilation. The Python interpreter goes line by line and
compiles/executes the code it finds. Interpreted languages are easier to test modularly, but you lose the benefit
of having a compiler check for mistakes for you
"""

"""
There are three specific naming conventions to follow when writing python code

Classes and Object: PascalCase (unique words have their first letter capitalized, no spaces between words)

Constant Values: SCREAMING_SNAKE_CASE (everything is capitalized, underscores separate unique words)

ANYTHING ELSE: snake_case (no capital letters, underscores separate unique words)
"""

"""
In Python it is easy to create variables that our code can work with. Variables are useful when you don't know the
exact values you are going to work with, but you know the general information about what they will represent. To
create your variable you first give it a name, and then you use the = and on the right side of the = you put the
value that your variable will represent
"""
name = "Eric Suminski"
print(name)

"""
By themselves, variables don't do much: where it gets interesting is when they are passed into control-flow
statements.
"""

name = "Not Eric"
if name == "Eric Suminski":
    print(name)

"""
Notice our if statement has a colon at the end of it, and the print statement that comes after it is indented. This
is how Python determines what code belongs in a statement: it uses indentation to determine what code is controlled
by your control-flow statements
"""

name = "Eric Suminski"
if name == "Eric Suminski":  # if this statement is true, then a boolean True is returned
    if 5 + 5 == 10:  # notice we can make calculations in our if statements
        if "a" == "a":
            if True:  # True is a boolean value, adding it to my if statement gurantees that we move to the next block of code
                print("that is a lot of indents")

"""
If statements are checking to see if their statement returns a boolean true or not. A boolean true is a logical true,
which can sometimes get a little tricky
"""
if 5 + 5 != 11:  # this produces a True boolean, because 5 + 5 does not equal 11
    print("The logic is consistent")
"""
You can add an else statement to your if statements. This will make a different block of code execute if your if
statement returns a False boolean
"""

if 5 + 5 == 11:
    print("that does not look right")
else:
    print("5 + 5 does not equal 11")
