"""This module contains some exercises to help you better understand and work with Flask"""
from flask import Flask, request, jsonify

"""
In this module, half of the exercises require you to finish writing functions for routes that are already created, and
the other half requires you to create the route for the already implemented function. Use the comments provided in
each exercise to figure out what material is missing, and then add it to make each HTTP handler complete. Use Postman
to test your work.

All return values should be stored in JSONs, each possible return value should be tested for in Postman.
"""

# use this flask object
app: Flask = Flask(__name__)

"""
Routes that need functions implemented
"""


@app.route("/greeting", methods=["GET"])
def basic_greeting():
    """this function should return a general greeting"""
    pass


@app.route("/greeting/<name>", methods=["GET"])
def personalized_greeting(name: str):
    """this function should return a personalized greeting based upon the name provided as a path param"""
    pass


@app.route("/add/<num_one>/<num_two>", methods=["GET", "POST", "PATCH"])
def variable_math(num_one: str, num_two: str):
    """this function should do addition if it is a get request, multiplication if a post request, or subtraction if
    it is a patch request """
    pass


"""
functions that need routes implemented
"""

list_for_exercises = ["Hello", "world", "!"]


# @app.route()
def return_element_from_list(index: str):
    """this function should return the object at the given index position from the list above"""
    try:
        return_message = {"message": list_for_exercises[int(index)]}
        return_json = jsonify(return_message)
        return return_json, 200
    except IndexError as e:
        return_message = {"message": str(e)}
        return_json = jsonify(return_message)
        return return_json, 404


# @app.route()
def add_element_to_list():
    """this function should add an object provided in the http request body to the list above"""
    body = request.get_json()
    list_for_exercises.append(body["object"])
    return jsonify({"message": "object has been added to the list"}), 201


# @app.route()
def remove_element_from_list(index: str):
    """ this function should remove an object at the given index position from the list above"""
    try:
        del list_for_exercises[int(index)]
        return jsonify({"message": "element deleted successfully"}), 200
    except IndexError as e:
        return jsonify({"message": str(e)}), 404
