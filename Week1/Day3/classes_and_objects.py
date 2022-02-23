"""this module has notes and examples for Python classes and objects"""
from abc import ABC, abstractmethod  # we are referencing abstractmethod, not calling it here

"""
Everything in Python is an object, and all these objects need to have an associated class. A Class is like a blueprint:
it lets your program know what kinds of behaviors and states your object can have.
"""


class MyFirstClass:

    # I want this to have a string and int variable attached to it
    # You can only have one of these defined at a time
    def __init__(self, my_string_variable: str, my_integer_variable: int):
        # you don't have to name them the same, but it helps reduce confusion to give them the same name
        self.my_string_variable = my_string_variable
        self.my_integer_variable = my_integer_variable
        self.my_boolean = True


my_first_object = MyFirstClass("My first object string", 10)
my_second_object = MyFirstClass("My second object string", 20)

print(my_first_object.my_string_variable)  # this will print the string for object 1
print(my_second_object.my_string_variable)  # this will print the string for object 2

"""
As we can see above, there is not much you NEED to do to make a custom class in Python. You use the class keyword
to declare that you are making a class, give it a name following PascalCase naming convention, and then make sure
to give it a dunder __init__ method to control how you create objects of your custom class. Any class fields can
be declared in the init method.
"""

"""
You can create multiple kinds of classes in Python, one of the more common options is the abstract class. In the
example above we created a regular class: we can create objects out of it, we can access its properties, it works
just like any other regular class in Python. There are also classes called Abstract classes: these are useful
when you need code to be available for multiple classes, but implemented in different ways
"""


class MyAbstractClass(ABC):

    @abstractmethod
    def my_abstract_method(self, input_one, input_two):
        pass


"""
Right now, this abstract class is not doing anything. To do something with it, we need to create new classes that
are able to inherit from this abstract class
"""


class ClassOne(MyAbstractClass):
    # I want this to do division
    def my_abstract_method(self, input_one, input_two):
        return input_one / input_two


class ClassTwo(MyAbstractClass):
    # I want this to do string concatenation
    def my_abstract_method(self, input_one, input_two):
        return str(input_one) + str(input_two)


object_one = ClassOne()  # here i am creating an object of ClassOne
object_two = ClassTwo()  # here I am creating an object of ClassTwo

print(object_one.my_abstract_method(10, 5))  # this will print 2.0
print(object_two.my_abstract_method(10, 5))  # this will print 105

"""
In the example above we can see that, despite each object calling the same method, we get different outputs. This
is why abstract classes are so valuable: they allow us to change the implementation of our methods to fit our needs
"""

"""
Also, in the example above we used typecasting to make sure that our ClassTwo was doing string concatenation and
not regular addition. This is a useful tool when you want to make sure you are working with a specific datatype

If we want to, we can also inherit regular classes
"""


class ParentClass:
    def __init__(self, parent_variable):
        self.parent_variable = parent_variable
        print("The parent init dunder method was called")

    def parent_method(self):
        print("this method comes from the parent class")


# this class inherits all the states and behaviors of its parent class
class ChildClass(ParentClass):

    def __init__(self, child_variable, parent_variable):
        super().__init__(parent_variable)
        self.child_variable = child_variable
        print("the child init dunder method was called")


my_child_object = ChildClass("this belongs to the child variable", "this belongs to the parent variable")
# running the module will print out the messages in both parent and child init dunder methods

my_child_object.parent_method()

"""
We have already looked at regular and abstract methods, but there are two other kinds of methods to be aware of.
The first one is class method
"""


class UsingClassFields:

    class_count = 0

    def __init__(self):
        UsingClassFields.class_count += 1
        print(f"The class count is now {UsingClassFields.class_count}")

    @classmethod
    def get_class_count(cls):
        return cls.class_count


checking_class_variable_object_one = UsingClassFields()
checking_class_variable_object_two = UsingClassFields()

print(checking_class_variable_object_one.class_count)