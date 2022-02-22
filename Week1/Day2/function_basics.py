"""This module has notes and examples concerning functions and methods"""

"""
functionally, functions and methods are the same thing: they are a reusable piece of code. The main difference is that
a method is a function that is attached to an object: you can't use it without an object present.
"""

print("I can do this without having to create an object")  # this is a FUNCTION

my_string_object = "     This string has many attached methods"

print(my_string_object.strip())  # this down here is a METHOD

"""
It is nice that Python provides many built in functions for us, but sometimes we need to creat our own custom functions.
We can do this by using the def keyword
"""


# if I want to create a custom function, i need to follow this format: def function_name(parameters):

def my_special_addition_function(number_one, number_two, number_three):
    # to make my function actually functional, I need to assign the value of this addition to a new variable
    addition_result = number_one + number_two + number_three
    # now I want to get this value back, so I need to use the return keyword to get it out of my function
    return addition_result


# by itself, this actually does not do anything for my code: I need to do something with it
my_special_addition_function(1, 2, 3)

# I can assign it to a variable
result = my_special_addition_function(1, 2, 3)
print(result)

# I could print the value directly
print(my_special_addition_function(1, 2, 3))

"""
Something to keep in mind with functions: ALL functions actually have a return value, even if you don't assign one.
All functions by default return the data type None if you do not assign a return value.
"""


def my_no_return_value_function():
    print("I don't have a return value, or do it?")


my_no_return_value_function()
print(my_no_return_value_function())

"""
Keeping in mind that functions will return None if no return value is given can be helpful for your control flow
"""

"""
When working with functions it can sometimes be difficult to know what kind of data you are expecting to be passed
into your functions
"""


def is_this_math_or_concatenation(input_one, input_two):
    return input_one + input_two


print(is_this_math_or_concatenation(5, 5))
print(is_this_math_or_concatenation("Hello", " world!"))

"""
Python provides a way to reduce the ambiguity of your meaning when it comes to creating your functions. It does this
by allowing type annotation. Type annotations are great for reminding the developer what data types they are EXPECTING
to work with, but it actually has no effect upon your code at runtime.
"""


def this_function_is_meant_for_math(input_one: int, input_two: int) -> int:
    return input_one + input_two


print(this_function_is_meant_for_math("Hello ", "world!"))

"""
Sometimes you don't know how much data your function is going to work with: in these situations you can use the variable
argument parameter to handle this arbitrary amount of input
"""


def this_function_has_a_var_arg_parameter(*args):
    for element in args:
        print(element)


this_function_has_a_var_arg_parameter(1, 2, 3, 4, 5)
this_function_has_a_var_arg_parameter("Hello", " ", "world", "!")
this_function_has_a_var_arg_parameter(1, "Hello", 2, "world")
# it does not matter what type or how many objects you place inside your variable argument, they are all accessible

"""
Functions in Python can also have what is called kwargs, or key word arguments. These are values that are accessed via
their key words
"""


def show_username_and_password(**kwargs):
    print(kwargs["username"])
    print(kwargs["password"])


show_username_and_password(password="MySuperSecretPassw0rd", username="Mypublicusername")

"""
You can mix and match these different ways of creating your functions, but it must be in this order:
hard coded parameters, variable arguments, key word arguments
"""


def over_the_top_function_using_all_input_options(my_number: int, my_string: str, *everything_else, **kwargs):
    print(my_number)
    print(my_string)
    for element in everything_else:
        print(element)
    print(kwargs["my_key"])


over_the_top_function_using_all_input_options(1, "My string", 1, 2, 3, 4, 5, 6, "A string", 7, 8, my_key=True)
