"""This module contains information about scopes and namespaces in Python"""
from abc import ABC
name = "Eric" # this variable exists in the global scope

"""
The global scope is anything that is declared in the module without using any tabbing
"""

"""
The next level of scope is the local scope. This is typically code that is written inside of a function
or a method. The variables you declare inside of the function/method are only available within that function or 
method
"""

def showing_local_scope():
    y = 11 # this is local scope: this code is only available within the scope of this function
    print("I just set y to 11")

showing_local_scope()
# print(y) tryin this would actually produce a NameError because y is not defined within the global scope

"""
You may every now and then come across a situation where you have a function inside of another function. When this
happens, the outer function's local scope is actual enclosed scope: the inner function will have access to the
"local" scope of the outer function
"""

def outter_function():
    y = 11 # this is technically Enclosed scope: both the outer function and the inner function have access to this variable
    def inner_function():
        return y # I am able to return this value because this inner function has access to it
    return inner_function()

print(outter_function())

"""
There is a neat little trick you can do with global variables: you can access them without needing to pass them
into a function or method. You can do this by using the global keyword
"""

global_variable = 5

def add_five(input):
    print(input + 5)

add_five(global_variable)

def add_five_global_keyword():
    global global_variable
    print(global_variable + 5)

add_five_global_keyword()

"""
We have actually done this before: when we were working on abstract classes we had to import the abc module and then
import the ABC class from that module. The syntax we used was actually a shorthand for setting the namespace of the
data we wanted to work with
"""

class MyAbstractexample(ABC):
    pass

# if we just imported abc we could do the following: class MyAbstractClass(abc.ABC):