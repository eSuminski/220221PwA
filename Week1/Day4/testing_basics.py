"""This module contains introductory testing information and a basic app designed using Test Driven Development"""
import numbers
from abc import ABC, abstractmethod

"""
Testing is a fundamental part of development, quality assurance, really anything to do with software development. It
used to be that companies would hire manual testers to test their applications: they would manually check things
work as intended, and they would check and see if the software could handle user errors, wrong inputs, general
mistakes, code errors, etc. 

Enter automation testing: the benefit of automation testing is that you can do close to everything that a manual
tester can do, but you can automate the process and speed it up. For now, we will focus on automating one kind
of test: the unit test. When you do unit testing you are testing modular parts of your code individualy. Let's do
some unit testing
"""

"""
There are 4 steps to Test Driven Development

1. Create interfaces

2. create tests to validate functionality

3. implement interfaces (implement functionality) to pass your tests

4. repeat as necessary
"""

"""
Step 1: create interfaces
"""


# We are going to create a calculator using Test Driven Development, and we will use unit tests to make sure it does
# exactly what we want it to do

class CalculatorInterface(ABC):

    @abstractmethod
    def addition(self, number_one, number_two):
        pass

    @abstractmethod
    def division(self, number_one, number_two):
        pass

    @abstractmethod
    def round(self, number):
        pass

"""
Now that we have our interface (In Python it is an abstract class) we can create the skeleton of our implementation
class so that we are ready to go AFTER we have created our tests
"""

class CalculatorImplementation(CalculatorInterface):

    # these methods should only work with integers: we don't want to mess with fractions or anything else
    # also, it should only work with positive numbers
    def addition(self, number_one, number_two):
        if isinstance(number_one, int) and isinstance(number_two, int): # this line is checking the input types
            if number_one > 0 and number_two > 0: # this line checks that we are working with positive numbers
                return number_one + number_two
            else:
                return "bad input: please only enter whole positive numbers" # this is returned if we have a 0 or less input
        else:
            return "bad input: please only enter whole positive numbers" # this returns if we have non integer data types

    def division(self, number_one, number_two):
        try:
            if isinstance(number_one, int) and isinstance(number_two, int):  # this line is checking the input types
                # our business rules state we should not allow 0 values, but here I will to show testing for exception handling
                if number_one >= 0 and number_two >= 0:  # this line checks that we are working with positive numbers
                    return number_one / number_two
                else:
                    return "bad input: please only enter whole positive numbers"  # this is returned if we have a 0 or less input
            else:
                return "bad input: please only enter whole positive numbers"  # this returns if we have non integer data types
        except ZeroDivisionError:
            return "You can't divide by zero"

    # you need to work with floats to round your number, so it is ok for this method to receive fraction input, and
    # to take it a step further, we don't want whole numbers to be allowed in the method
    def round(self, number):
        if isinstance(number, float):  # this line is checking the input types
            if number > 0:  # this line checks that we are working with positive numbers
                return round(number)
            else:
                return "bad input: please only enter mixed positive numbers"
        else:
            return "bad input: please only enter mixed positive numbers"


"""
Now that we have our skeleton to work with, we can start crafting our tests: see module called test_calculator inside
the tests_for_calculator package
"""