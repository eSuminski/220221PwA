"""this module contains some exercises to help you become more familiar with stubbing"""

"""
Below are 3 functions that, in order to perform true unit testing, require the use of stubbing. The functions have
already been implemented, you simply need to write the unit tests for them. In this case though, because each
function being tested calls an inner function, you will need to stub the results of the inner function in order to
create true unit tests.

for each function named "function_to_test" create a unit test for each possible return value
"""


def inner_function_one(num_one: int, num_two: int) -> float:
    return num_one / num_two


def function_to_test_one(num_one: int, num_two: int) -> str:
    result = inner_function_one(num_one, num_two)
    if result % 2 == 0:
        return "Even"
    else:
        return "Odd"


def inner_function_two(*words) -> list[str]:
    word_list = []
    for word in words:
        word_list.append(word)
    return word_list


def function_to_test_two(*words) -> str:
    result = len(inner_function_two(*words))
    if result <= 5:
        return "There are not that many words."
    else:
        return "There are a LOT of words!"


def inner_function_three(boolean: bool) -> str:
    if boolean:
        return "I want the truth!"
    else:
        return "You can't handle the truth!"


def function_to_test_three(boolean: bool) -> str:
    result = inner_function_three(boolean)
    if result == "I want the truth!":
        return "the boolean was true!"
    else:
        return "the boolean was false!"


"""
Write your unit tests below
"""
