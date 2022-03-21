"""This module contains some exercises for those who want more practice doing basic unit tests"""

"""
Similar to the reverse coding challenges you have done, these exercises have you work in reverse.
There are 5 functions present, each performing some different operation. Write out two tests for each function, 
one for each possible return statement
"""


def function_one(int_one: int, int_two: int) -> int | str:
    if type(int_one) is not int or type(int_two) is not int:
        return "Please provide two whole numbers"
    else:
        return int_one - int_two


def function_two(word_one: str, word_two: str) -> str:
    if type(word_one) is str and type(word_two) is str:
        return word_one + word_two
    else:
        return "please provide two string inputs"


def function_three(list_of_objects: list) -> str:
    if len(list_of_objects) == 0:
        return "There are no objects in this list"
    else:
        return f"there are {len(list_of_objects)} objects in this list"


def function_four(**kwargs) -> str:
    if kwargs["username"] == "Lucky" and kwargs["password"] == "Stars":
        return "validation complete: welcome back William Thatcher!"
    else:
        return "You have been weighed, you have been measured, and you have been found wanting"


def function_five(float_as_str: str) -> str | int:
    if type(float_as_str) is not str:
        return "Please provide a valid mixed number as a string"
    else:
        return round(float(float_as_str))


"""
Write your tests below
"""