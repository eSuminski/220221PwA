"""this module contains some exercises to help you become more familiar with mocking"""

"""
These are the same functions as those in the stub_practice module, but in this module, you need to write some mock 
tests instead of stub tests. As a reminder, mock tests check the path of execution of the function, not the outcome.

for each function named "function_to_test" create a mock test for each possible return value (check that the inner
function was called with the correct input). Remember to have your inputs and return values match as closely 
as possible to a real use scenario.
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
Write your mock tests below
"""
