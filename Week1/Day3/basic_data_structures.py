"""This modules contains notes and examples for Lists, Sets, Tuples, and Dictionaries"""

"""
Bar none, the most common data structure you are going to see in Python is the List. Lists are mutable, they allow
duplicates, and you can access the elements inside of them via their index position
"""

my_empty_list = []  # this creates an empty list

my_list_of_numbers = [1, 2, 3, 4, 5]  # this creates a list with the numbers 1-5 inside

my_list_of_strings = ["one", "two", "three"]  # this creates a list with three strings inside

my_string = "I am going to add this to a list"
my_soon_to_be_full_list = []

print(my_soon_to_be_full_list)
my_soon_to_be_full_list.append(my_string)  # the append method adds objects to our list
print(my_soon_to_be_full_list)

"""
There are a few ways you can access your information inside your list
"""

print(my_soon_to_be_full_list)  # this will return the list itself, so I can see all its content
print(my_soon_to_be_full_list[0])  # this is the easiest way to get an element from the list: use its index position
# print(my_soon_to_be_full_list[1]) will give an IndexError because this index position does not exist... yet

my_soon_to_be_full_list.append("this is another string")
my_soon_to_be_full_list.append(10)  # notice that I can mix and match object types inside my list

print(my_soon_to_be_full_list)

my_soon_to_be_full_list.insert(1,
                               5)  # this inserts, does not replace. Scoots everything after the given index up by one index position

print(my_soon_to_be_full_list)

"""
If you want to directly replace something inside of your list you can, just like when you are trying to get information
out of the list, reference the index position and instead assign it a new value
"""

my_list_that_has_numbers = [2, 5, 6, 8, 10]
my_list_that_has_numbers[1] = 4
print(my_list_that_has_numbers)

"""
List objects have a few more methods that are handy to know: for instance, there is an easy way to transfer the
content of an iterable object to your lists: the extend method
"""

list_one = [1, 2, 3]
list_two = ["1", "2", "3"]
# for element in list_two:
#     list_one.append(element)
# I don't want to write two lines of code: let's do it in one
list_one.extend(list_two)  # the extend method takes in an iterable object and appends its content to your list
print(list_one)

"""
The remove method will go through your list and remove the first element that matches the argument given for the
method
"""

list_one.remove("1")
print(list_one)  # this is useful when you only have one object that meets the criteria for your remove method

list_one.insert(3, "1")
list_one.insert(3, "1")

# for index_position in range(len(list_one)-1,0,-1):
#     if list_one[index_position] is "1":
#         del list_one[index_position]
#         break # this exits the loop after the first deletion
# added this because someone asked how to reverse the remove method

list_one.remove("1")  # because I added two "1" there is still going to be one remaining after the remove method
print(list_one)

# list_one.remove("4") will give a ValueError

"""
Sometimes you need to clear out everything inside of your list. To do this you use the clear method
"""

temp_list = list_one.copy() # use copy when you want a NEW collection of the data stored in a seperate data structure
list_one.clear()
print(list_one)
list_one = temp_list

"""
If you ever need to know how many instances of an object you have in your list you can use the count method
"""

print(list_one.count("4"))  # returns how many instances of the argument are inside the list

"""
you can use the index method to check subsection of your list
"""
# index(value we are looking for, index start position, index end position)
print(list_one.index("1", 2, 4))  # this will return 3 because "1" is located at index position 3
# print(list_one.index("$",2,4)) this will create a ValueError because the dollar sign is not in my list

"""
You will find that working with sorted lists is a better experience 99/100 times. Python provides a built in
method for lists that can do this for you called sort()
"""

my_unordered_list = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10]
print(my_unordered_list)
my_unordered_list.sort()
print(my_unordered_list)
my_unordered_list.sort(reverse=True)
print(my_unordered_list)

my_unordered_string_list = ["bannana", "carrot", "apple"]
my_unordered_string_list.sort()
print(my_unordered_string_list)
my_unordered_string_list.sort(reverse=True)
print(my_unordered_string_list)

my_complicated_unordered_list = [[1,"c"], [3, "a"], [2, "b"]]


def my_key(element):
    return element[0] # this is redundant because it is the default way of checking


my_complicated_unordered_list.sort(key=my_key)

print(my_complicated_unordered_list)

def my_string_key(element):
    return element[1]

my_complicated_unordered_list.sort(reverse=True, key=my_string_key)

print(my_complicated_unordered_list)

"""
In the above examples we saw that you can use the sort method to take an unorganized list and make it organized.
You can even do this with complicated objects by using a key, which is usually a function that returns a specific
value from the elements in the list. You can also use the reverse key word argument and set it to true to make
the sort method sort the obbjects from highest to lowest value
"""




