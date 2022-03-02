"""this module contains the api for my application"""
from flask import Flask, request

app: Flask = Flask(
    __name__)  # passing __name__ as an argument lets the object know it should look for it's information in this module

my_list = ["I love my dog", "I ate fish for lunch today", "I wish I was still asleep"]


@app.route("/greeting", methods=["GET"])
def hello_world():
    return "Hello world!"


@app.route("/personal/<name>", methods=["GET"])
def personal_greeting(
        name: str):  # ANYTHING that comes as a path parameter will be passed into your function as a string
    return f"Hello {name}!"


@app.route("/add/<num_one>/<num_two>", methods=["GET"])
def addition_function(num_one: str, num_two: str):
    result = int(num_one) + int(num_two)  # since these numbers are coming in as strings we need to type cast them
    return str(result)  # we then need to typecast the number back into a string to return it to the requester


@app.route("/list/<index>", methods=["GET"])
def get_phrase_from_list(index: str):
    global my_list
    return my_list[int(index)]

@app.route("/list", methods=["POST"])
def add_phrase_to_list():
    request_content = request.get_json() # this method turns our JSON into a python dictionary
    global my_list
    my_list.append(request_content["key"])
    return "Phrase added successfully"


app.run()
