"""This module continues the Test Driven Development of our calculator app"""
from testing_basics import CalculatorImplementation

"""
Whatever you decide to call your module, make sure it starts with test_ because pytest, when it runs
all of our tests, will be looking for modules that start with test_ to find the actual unit tests
"""

"""
Pytest will consider any and all tests to pass if they do not raise an exception. So, we can use the assert keyword
to force our test to raise an exception if an evaluated condition returns a false boolean
"""

# let's start by making some tests for addition

calculator = CalculatorImplementation()


def test_addition_success():  # this is our test declaration, make sure to call it test_
    result = calculator.addition(5, 5)  # here we assign the return value of our method to a variable called result
    assert result == 10  # if this is true, then I will get a True boolean back, else an AssertionError will be raised
    # our test will pass if no exceptions are raised


# what might I need to test to make sure our addition method is only working with integers?
# what happens when a float is provided? One or both inputs?
# what happens when strings are provided instead of ANY kind of number type?
# what happens if someone tries to use negative numbers?



"""
We will work with these other methods later
"""

def test_division_success():
    result = calculator.division(10, 5)
    assert result == 2


def test_round_success():
    result = calculator.round(1.1)
    assert result == 1