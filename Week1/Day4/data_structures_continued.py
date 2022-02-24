"""This module contains notes and examples about Sets, Tuples, and Dictionaries"""

"""
While lists give you great flexibility in the way you use them, sometimes it can be helpful to use a data structure
that provides more restrictions. Sets are a great way of providing a restriction in your code: Sets do not allow duplicates
to be stored inside of them. A unique feature of Sets is that they are not indexable.
"""

my_set = {"1"} # if I left this empty Python would think it was a Dictionary, not a set
two = "2"
three = 3
four = "four"
i = "i"
declare = "declare"
a = "a"
thumb = "thumb"
war = "war"

"""
to add information to a set you use the add method
"""

my_set.add(two)
my_set.add(three)
my_set.add(four)
my_set.add(i)
my_set.add(declare)
my_set.add(a)
my_set.add(thumb)
my_set.add(war)

print(my_set) # we will get a different order every time we run our code because Sets do not maintain order of insertion

my_ordered_set = {1}
my_ordered_set.add(2)
my_ordered_set.add(3)
my_ordered_set.add(4)
my_ordered_set.add(5)
my_ordered_set.add(6)
my_ordered_set.add(7)
my_ordered_set.add(8)
my_ordered_set.add(9)
my_ordered_set.add(10)
my_ordered_set.add(11)
my_ordered_set.add(12)

print(my_ordered_set) # these numbers will be ordered, but this is not the norm.

"""
Since we don't have access to index positions we have to access our data a different way. One way is to use the
pop method
"""

# print(my_set[0]) this will give us a TypeError because we can't use index positions when getting items from Sets

# print(my_set.pop())
print(my_set)

"""
to get specific information you would need to actually iterate through your set to get it
"""
for element in my_set:
    if element == "four":
        print("I found what I wanted to get specifically")

"""
If we want to remove specific information from our set we can either use the discard method or the remove method. The
difference between the two is that one will give you an error if the object you are looking for does not exist
in the set, the other is ok with the object not existing
"""

my_set.discard(four)
# my_set.remove(four) If I try running this I will get a KeyError because the variable four is not in the set

"""
So when to use discard/remove? Remove is going to be useful when you actually need to know if some data was not
removed from the set. This is useful in situations where your code must be able to adjust on the fly to receiving
this kind of "false" information (I wanted to remove data a, which does not exist, so I need to actually do something
about that). Discard is going to be useful in just about every other situation.
"""

"""
Sometimes it can be useful to add large groups of data into your sets: you use the update method when you want to
transfer data from one iterable collection to your set
"""

rest_of_phrase = [5,6,7,8, "try to keep your thumb straight"]

my_set.update(rest_of_phrase)
print(my_set) # this now has the information from the rest of phrase list

"""
Another data structure you should be aware of is Tuples. Tuples are immutable data structures that allow for duplicate
objects to be stored in them, and you can access those objects via their index position.
"""

my_tuple = ("this", "is", "it")

print(my_tuple.count("is")) # this will check how many instances of the string "is" I have

print(my_tuple.index("this")) # this will return 0 because the string "this" is located there

print(my_tuple[2]) # because tuples are indexable we can access objects via their index position

"""
One way in which you can utilize tuples is with the enumerator object. 
"""

my_list = [2,5,7,3,1,3,6,8,9,9]
enumerated_list = enumerate(my_list)
print(enumerated_list)
print(list(enumerated_list))

adjusted_enumerated_list = enumerate(my_list,52) # you can adjust the enumerate matching number, which is sometimes helpful
print(list(adjusted_enumerated_list))

"""
This is a little trick you can use when you don't have direct access to your index positions: you can turn your
data collection into an enumerate object, typecast that object into a list, and then you will have both the
elements inside of the data collection, and the location where they were found
"""

"""
Dictionaries, at their core, are just key value pairs. They are an object that assigns keys to different values
that makes it easy to access the values.
"""

def key_function():
    return "this function is going to act as my key"

my_dictionary = {
    "key":"value",
    1:"this value is associated with the key 1",
    key_function(): "this value is associated with key_function()",
    True:key_function()
}

print(my_dictionary["key"])
print(my_dictionary[1])
print(my_dictionary[key_function()])
print(my_dictionary["this function is going to act as my key"])
print(my_dictionary[True])

"""
Normally when you make a dictionary you will want to create it like the one below: make the value of the key an
obvious connection to its paired value
"""

number_dictionary = {
    "one":1,
    "two":2,
    "three":3
}

"""
There are some limitations to what you can do with dictionaries: the main one is that you can not have duplicate
keys inside of your dictionary (but you can have duplicate values)
"""

duplicate_key = {
    "one": 1,
    "one": 2 # if I do this I am reassigning the value, not making a duplicate

}

print(duplicate_key["one"])

"""
To make a new key/value pairing (or to reasign a key/value pair) you use square brackets, place the key inside
those brackets, and then use the assignment operator to assign a value
"""

duplicate_key["two"] = 2

duplicate_key["two"] = "2"

"""
To see the keys and values paired together you can use the items method, for just keys you use the keys method, and
for values you use the values method
"""

print(duplicate_key.items()) # this returns the key value pairs inside tuples
print(duplicate_key.keys()) # this returns the keys inside a list
print(duplicate_key.values()) # this returns the values inside a list

for key in duplicate_key.keys(): # you can use these methods and then loop through their content
    print(key)

for key, value in duplicate_key.items(): # this is a shorthand way to access the key and value inside the tuple
    print(key, value)

"""
To delete a key from your dictionary you use the del keyword
"""

del duplicate_key["one"] # I am going to delete the key I declared here
print(duplicate_key.items())

"""
There is a helpful method called the setdefault method. This method can do multiple things for you: if the key
you are trying to access exists already then you will get its associated value back. If it does not exist, you can
set the value that you wish for a new key to have inside of your dictionary with the key you provided the method
"""

print(duplicate_key.items())
print(duplicate_key.setdefault("two","i want this to be the value"))
# print(duplicate_key["one"]) If I try to access a key that does not exist I will get a KeyError
print(duplicate_key.setdefault("one","This did not exist a moment ago"))
print(duplicate_key.items())

