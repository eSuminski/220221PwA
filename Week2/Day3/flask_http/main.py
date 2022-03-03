"""this module contains the api for my application"""
from flask import Flask, request, jsonify

app: Flask = Flask(
    __name__)  # passing __name__ as an argument lets the object know it should look for its information in this module

# this list will act as our database
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


@app.route("/list", methods=["GET"])
def get_all_phrases_from_list():
    global my_list
    my_json_list = jsonify(my_list)
    return my_json_list, 200


@app.route("/json", methods=["GET"])
def return_a_json():
    customer_id = 1
    first_name = "Ted"
    last_name = "Teddington"

    # because this will be converted to a JSON we should follow JSON naming conventions
    customer_as_dictionary = {
        "customerId": customer_id,
        "firstName": first_name,
        "lastName": last_name
    }

    # we use the jsonify method to convert our dictionary into a json
    customer_as_json = jsonify(customer_as_dictionary)
    return customer_as_json, 200


@app.route("/list", methods=["POST"])
def add_phrase_to_list():
    request_content = request.get_json()  # this method turns our JSON into a python dictionary
    global my_list
    my_list.append(request_content["key"])
    return "Phrase added successfully"


@app.route("/query", methods=["GET"])
def get_filtered_phrases():
    min_index = request.args["min"]
    max_index = request.args["max"]
    global my_list
    return_list = []
    for index in range(0, len(my_list), 1):
        if index >= int(min_index) and index <= int(max_index):
            return_list.append(my_list[index])
    return_list_as_json = jsonify(return_list)
    return return_list_as_json, 200


app.run()
