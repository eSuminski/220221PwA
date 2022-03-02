"""this module contains some reminders about the different data structures"""

my_dictionary = {
    "key 1":1,
    "key 2":2,
    "key 3":False
}

print(my_dictionary["key 1"]) # I place the key instead of an index position to retrieve the associated value

my_dictionary["key 4"] = 4 # this is a simple way to assign a value to a key, whether that key already exists or not

"""
Lists are your most flexible data type: they allow duplicates, you can access elements via their index position, and
you can adjust their size dynamically.
"""

my_list =[]

my_list.append(1) # the empty list now has an int object at index position 0
my_list.append(1) # this puts it at index position 1

print(my_list[0]) # this returns the value at index position 0

"""
Sets are a little different, because they do dynamically resize, but you can not access elements by an index 
position, and you can't place duplicates inside of your set.
"""

my_set = {1} # be careful: empty {} will be considered dictionaries by default in python

my_set.add(1)

print(len(my_set))

"""
Tuples are also unique in that they do not allow for new content to be added, or for content to be removed. They 
are immutable, but you can access elements by their index position, and you can have duplicate elements
"""

my_tuple = ("this", "is", "is", "it")

print(my_tuple[2])

"""
Pip is simply your package management system, and Pypi is where Pip looks for packages you want to install by
default

The main way we have been using pip is to gain access to the pytest, and after today, the flask, packages so that
we can incorporate them into our code. To do this, we simply use the pip command, the install keyword, and then the
name of the package of code we want to install

example: pip install pytest will install the pytest package from Pypi into our project's virtual environment.

if you don't know the name of the package you want, you can look it up on the Pypi website and it will give you
the actual pip install command you need to run to get the code
"""

"""
The virtual environment is simply a way to keep your computer from becoming cluttered with unnecessary python 
packages. You will often find when working with Python code that you need specific downloads from Pypi that will
only be relevant to the specific project, and you won't need that code when you are done with the project. If you
were installing those packages from Pypi directly to your global python storage, this would start to eat up memory
very quickly, and would make navigating your global packages very clunky. To avoid this problem you can create
a virtual environment and have pip install all of your packages to that location instead of your global space.
"""