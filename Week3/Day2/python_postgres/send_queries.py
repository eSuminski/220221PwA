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
    cursor.execute(sql,(person.first_name, person.last_name))
        # commit our query
    connection.commit()
        # end our function
        # tuple_info = cursor.fetchone()
        # new_id = tuple_info[0]
    new_id = cursor.fetchone()[0]
    person.person_id = new_id
    return person

my_person = Person(0,"Sam", "Suminski") # this is my person object i will pass into the function
print(create_person_entry(my_person)) # this will print the values off the object that is passed into the database
