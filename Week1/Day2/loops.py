"""This module contains notes and examples about looping your code in Python"""

# print("I want this to print 5 times")

"""
I COULD write out five print statements to make my statement print 5 times, but what if I want to change it to
six loops? Am I going to manually change my code every time I change the ammount of times I want to loop my print
statement? This is inefficient and tiresome: we will instead use a for loop
"""

# to loop my print statement 5 times I am going to use the "for" keyword and the range method and the "in keyword

for loop in range(5):
    print("I want this to print 5 times")

"""
Let's break down what is happening in this loop:

for: the for keyword is used when you want Python to know that you are going to loop FOR a set interval

loop: this is a variable I declare that will represent whatever thing we are looping through/for

in: this keyword lets Python know that our loop is being facilitated by whatever entity comes next

range(#): this function is an easy way to control how many times your code is going to loop. The most basic way of
using it is to enter in a number that represents how many times you want your code to loop
"""

"""
It can be a little confusing how this loop is working, so lets actually print the value of "loop"
"""

for loop in range(5):
    print(loop) # When we run this the numbers 0 - 4 will print

"""
If you want to change the starting point of your range you can set it by first deciding on the number you want to
start at, and then put the number you want your range to go UP TO, but not include
"""

for loop in range(1,5): # Here we start at the number 1, and loop up to the number 5, but don't include it
    print(loop)

"""
Sometimes we don't want to loop by iterations of one, sometimes we need to go two or three iterations at once. We can
control this with the third input for the range function
"""

for loop in range(0,11,2): # (start, UP-TO but not including, increment value)
    print(loop)

"""
You don't just have to count up with the range function: you can also work backwards
"""

for loop in range(10, 4, -1):
    print(loop)

for loop in range(10,-1,-1):
    print(loop)

"""
Remember: range(#) sets the up-to end point, range(#,#) sets the start and up to end point, range(#,#,#) sets the start,
up to end, and increment value
"""

"""
There is another way of looping your code, and that is by using the "while" keyword. Unlike the for key word, the while
key word does not automatically assume you are looping through a collection of data
"""

# x = 5
# while x <= 10:
#     print(x)
# commented this out so my next example will actually run

"""
The example above is what is known as an infinite loop: because x always equals 5, and 5 is always less than or equal to
10, my code will forever and always print the value of x to the terminal. If you ever accidentally create an infinite
loop, you can use ctr + c to kill the operation and end your program
"""

x = 5
while x <= 10:
    print(x)
    x += 1
    # another way to do this: x = x + 1

"""
So when to use while, and when to use for? Generally speaking, if you need to loop through a set of data, use the for
loop. For loops have built in functionality and syntax that works will with data sets. When you need to find and/or
do something with data inside of a data collection, use the for loop.

While loops are useful in just about any other situation not covered by the for loop. While loops are useful when you 
need to loop your code an arbitrary number of times. Because it is not limited by the scope of whatever data collection
you are potentially working with (if you even are working with a data set), you can let your loop be more flexible 
in its implementation.
"""