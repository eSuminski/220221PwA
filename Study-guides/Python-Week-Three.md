### Mocking vs Stubbing
Stubbing is when you create a fake response for a method call: you create a mock of the class or method you need to stub, indicate what its return will be, then pass that result into your test. This is great for creating unit tests for anything that has buisness logic above the repository layer of your application. Sometimes, however, this is not enough: what if a bit of code was mistyped in the method you are stubbing and it never actually gets called? Your stub creates a predetermined response whether your code works as intended or not. This is where mocks come in: mocks can VERIFY the state and behavior of an object. Did the object actually call that second level function? Did the value of its "name" string actually change to what we want it to be? This works a litte differently than stubbing because it is no longer the return value alone you are interested in: it is the path to the result you are interested in.

### Positive vs Negative Test
Positive tests are those that check to see if your functions work as intended. If they receive the correct data, the correct response should be returned. Negative tests check to see if your function can handle things going wrong. This could be the wrong data being provided to your function, type discrepancies (wrong data type being passed as an argument, some sort of exception being raised), there are so many ways things can go wrong. Negative tests check to see if your functions can handle these situations

### Stubbing and Mocking in Python

```python
class Divider:
    def division(self, num):
        return num / 2

class Calculator:
    def __init__(self, divider: Divider):
        self.divider = divider

    def even_odd(self, num):
        try:
            if self.divider.division(num) % 2 == 0:
                return "even"
            else:
                return "odd"
        except ZeroDivisionError:
            return "You can't divide by zero!"

divider = module_a.Divider()
calculator = module_b.Calculator(divider)

"""
The two tests below are integration tests because they require both the even_odd and division methods to work
"""
def test_even_result():
    assert calculator.even_odd(12) == "even"


def test_odd_result():
    assert calculator.even_odd(10) == "odd"

"""
The two tests below are unit tests, because we stub the results of the division method to make sure we only check the string value that is returned
"""

def test_mock_even_result():
    calculator.divider.division = MagicMock(return_value=2)
    assert calculator.even_odd(10) == "even"


def test_mock_odd_result(our_mock):
    calculator.divider.division = MagicMock(return_value=3)
    assert calculator.even_odd(12) == "odd"

"""
the two tests below are also unit tests, but this time they are mock tests. We are making sure the division method is actually called, and that the correct value is passed into it
"""

def test_mock_verify_behavior():
    calculator.divider.division = MagicMock(return_value=3)
    result = calculator.even_odd(10)
    calculator.divider.division.assert_called()


def test_mock_verify_state():
    calculator.divider.division = MagicMock(return_value=3)
    result = calculator.even_odd(10)
    calculator.divider.division.assert_called_with(10)

"""
You can also use stubbing to raise an exception: you do this with the @patch annotation, pass a mock object into your test, and set its side effect to the particular exception you want raised
"""

@patch("package.module.Divider.division")
def test_catch_zero_division(mock):
    mock.side_effect = ZeroDivisionError()
    result = calculator.even_odd(0)
    assert result = "You can't divide by zero!"
```

### Psycopg
Psycopg is a Python package that provides tools for allowing your application to interact with a Postgres database. it makes use of a connection object to handle connecting your application to the database, and it provides the code for you send queries to the database.

```python
"""
First you need to create a connection object that contains all the necessary credentials for your database. It is good practice to hide those values, a common way of doing this is by using environment variables
"""

import os


def create_connection():
    try:
        # I am going to create a connection object that will handle all my queries to the database
        conn = connect(
            # host="endpoint goes here",
            # dbname="database type goes here",
            # user="username goes here",
            # password="password goes here",
            # port="port goes here"
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DBNAME"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as e:
        print(e)


connection = create_connection() # this gives us a global object we can import into other modules

print(connection) # this lets us test that we are successfully connecting to our intended database
```
Once you reach the point where you are able to send queries to your database you will import the connection variable you created and use it to call cursor(), execute(), and fetch() methods.
```python
"""Examples taken from the lecture notes"""
from manage_connection import connection


class Person:
    def __init__(self, person_id, first_name, last_name):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"person_id = {self.person_id}, first_name = {self.first_name}, last_name = {self.last_name}"


def create_person_entry(person: Person):
    # create sql query
    sql = "insert into persons values(default,%s,%s) returning person_id"
    # create cursor object to handle our query
    cursor = connection.cursor()
    # have cursor object send query to database
    cursor.execute(sql, (person.first_name, person.last_name))
    # commit our query
    connection.commit()
    # end our function
    # tuple_info = cursor.fetchone()
    # new_id = tuple_info[0]
    new_id = cursor.fetchone()[0]
    person.person_id = new_id
    return person


# my_person = Person(0,"Sam", "Suminski") # this is my person object i will pass into the function
# print(create_person_entry(my_person)) # this will print the values off the object that is passed into the database

def get_single_person_record(person_id):
    # create sql query
    sql = "select * from persons where person_id = %s"
    # create cursor object
    cursor = connection.cursor()
    # use cursor to execute sql query
    cursor.execute(sql, [person_id])  # for a single value, use a list instead of a tuple
    # create result set from my query
    person_record = cursor.fetchone()
    # parse that result set
    # person = Person(person_record[0], person_record[1], person_record[2])
    person = Person(*person_record)
    # return the parsed information
    return person


# print(get_single_person_record(1))

def get_all_person_records():
    sql = "select * from persons"
    cursor = connection.cursor()
    cursor.execute(sql)
    person_records = cursor.fetchall()
    person_list = []
    for record in person_records:
        person = Person(*record)
        person_list.append(person)
    return person_list


# for person in get_all_person_records():
#     print(person)

def update_person_record(person):
    sql = "update persons set first_name = %s, last_name = %s where person_id = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (person.first_name, person.last_name, person.person_id))
    connection.commit()
    # return person
    # return True
    return "Person updated successfully!"

# updated_info = Person(5, "Evil", "Bob")
# print(update_person_record(updated_info))

def delete_person_record(person_id):
    sql = "delete from persons where person_id = %s"
    cursor = connection.cursor()
    cursor.execute(sql, [person_id])
    connection.commit()
    return True

print(delete_person_record(5))


```