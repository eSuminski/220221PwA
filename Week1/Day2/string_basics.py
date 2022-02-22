"""This module has notes about strings"""

"""
Just about every programming language can work with strings, so they are a very useful type of object to be familiar
with. There are three different ways of creating your basic string in python
"""

string_one = "this is one way to make a string, using quotation marks"
string_two = 'this is another way to make a string, using single quote marks'
string_three = """This is also a valid way to make a string variable.

You can make multi-line strings using triple quotes"""
'''
This is neat, I can do triple quotes with single quotes...

Anyways, there are many ways to manipulate your strings. The most basic way of doing this is called string
concatenation. This is simply taking multiple strings and combining them together
'''


name = "Eric"
greeting = "Hello"

print(greeting + name)
# Strings in Python are immutable: neither name nor greeting has changed its actual value
print(name)
print(greeting)

"""
Another way to perform string concatenation is to use an f string. an f string is just like a normal string, but you
add an f to the start of it, and you add {} where you want to add a variable as the value inside the string
"""

greeting_as_f_string = f"Hello {name}" # the f lets the interpreter know it is working with a formatted string
print(greeting_as_f_string)

"""
Another way to craft your strings dynamically is to use the format method. You add this on to the end of the string
declaration and it lets you add in unique values that do not need to be hard-coded in
"""
another_name = "Sam"

greeting_using_format_method = "Hello {} and {}".format(another_name, name)

print(greeting_using_format_method)

"""
So we know how to create strings, but sometimes we will want to work with subsets of our strings. There are all sorts
of reasons why we might want to do this, and we can check substrings by using string slicing
"""

string_to_slice = "  Hello Eric   "
print(string_to_slice[0:5]) # Here we want to get just the substring "hello"

"""
you can imagine that the string "Hello Eric" actually looks like this inside our code:
0:H
1:e
2:l
3:l
4:0
etc
etc
"""

for letter in string_to_slice:
    print(letter)


"""
We can easily reverse a string by using string splicing. Instead of incrementing the string by one, we increment it by
negative one. Just make sure to add the extra : that separate the starting and up to points
"""

for letter in string_to_slice[::-1]: # [starting index:up to end point:increment]
    print(letter)

"""
There are two very useful methods to be aware of when working with strings: strip and split. 
"""

"""
strip allows us to strip away characters and white space from a string
"""

print(string_to_slice) # this prints our string like normal, all the white space present
print(string_to_slice.strip()) # this by itself will just remove any opening and trailing whitespace
print(string_to_slice.strip("H c")) # we can remove specific characters from the start and end of our string
print(string_to_slice)

"""
The strip method is useful when we want to get rid of extraneous elements inside our string. This does not actually 
change the string, but it does affect how our code will interact with the string. The input of string characters into
the strip method does not matter.
"""

"""
Another useful method is the split method: this is useful when you want to find all the sub strings inside of your
main string and do something with them
"""

very_long_string = "This is my very long string. I have lots of words in here"
print(very_long_string)
print(very_long_string.split()) # by default, this seperates all substrings by whitespace
print(very_long_string.split("i"))
print(very_long_string.split("is")) # unlike the strip method, split looks for exactly what you provide it

# here is a simple example of how you can use the split method to break a string into smaller parts to check
my_python_variable = "this_is_my_variable"
for word in my_python_variable.split("_"):
    for character in word:
        if character is "a":
            print("this is a bad name for a python variable!")