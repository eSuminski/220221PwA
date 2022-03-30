"""This module can be used in conjunction with the for_fetch.html file to see how you can create an http request body"""
from flask import Flask, request, jsonify
from flask_cors import CORS

"""
Make sure you have flask and flask-cors installed from pypi
"""
app: Flask = Flask(__name__)
CORS(app) # use this to avoid cors errors


@app.get("/<name>")
def get_greeting(name: str):
    return jsonify({"message": f"Hello {name}"}), 200


@app.post("/body")
def sending_http_request_with_body():
    body: dict = request.get_json()
    for message in body.values():
        print(message)
    return "done!"


app.run()
