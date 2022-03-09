"""This module has basic stubbing information and examples"""
from unittest.mock import MagicMock

"""
You can ask 10 different developers what stubbing and you will get 10 different answers. For our purposes, when I talk
about stubbing I am talking about "faking" function return values in order to perform unit testing. This is particularly
useful when writing unit tests for service layers of web applications that are connected to databases.
"""


class Divider:
    def division(self, num):
        # because my division method is not implemented correctly, integration tests wil fail
        return "this will not give me a remainder"


class Calculator:
    def __init__(self, divider_obj):
        self.divider_object: Divider = divider_obj

    def even_odd_check(self, num):
        if self.divider_object.division(num) % 2 == 0:
            return "Even"
        else:
            return "Odd"

divider = Divider()
calculator = Calculator(divider)

"""
The tests written below, although they do pass, are not true unit tests: because the division method attached to the
divider object is being called, it is part of the test, and so I am actually performing what is called a integration
test. 
"""

def test_get_even_regular():
    result = calculator.even_odd_check(8)
    assert result == "Even"

def test_get_odd_regular():
    result = calculator.even_odd_check(11)
    assert result == "Odd"

"""
Python has a built in system for creating unit tests from potential integration tests: the easy way to do this is
to use MagickMock
"""

def test_get_even_stubbing():
    calculator.divider_object.division = MagicMock(return_value=2)
    result = calculator.even_odd_check(11)
    assert result == "Even"


def test_get_odd_stubbing():
    calculator.divider_object.division = MagicMock(return_value=5)
    result = calculator.even_odd_check(423048)
    assert result == "Odd"