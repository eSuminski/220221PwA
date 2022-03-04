# HTTP/REST/FLASK

## HTTP intro
Hyper Text Transfer Protocal is the most common way of sending information over the web. It is a request/response system that will always give the requester a response, even if that response is only to say that everything that could have gone wrong did go wrong. There are two parts to HTTP: the request and the response
- HTTP Request anatomy
    - HTTP Version 
    - URL
        - the URL is what you see at the top of your browser: we will focus on domain name, port, path, and params
![image from Mozilla Firefox ](url-example.png)
    - VERB
        - the verb provides context for what your request is trying to do
            - GET
            - PUT
            - POST
            - PATCH
            - DELETE
    - HEADERS
        - the meta data of the request
    - BODY
        - This is the content of your request. GET requests do not have a body
The HTTP response is a little different from the request
- HTTP Response anatomy
    - HTTP Version
    - HEADERS
        - the meta data of the reponse
    - BODY
        - this is whatever data is being returned within the request, if any is provided
    - STATUS CODE
        - this code represents how the request was handled (successfuly, failed, transfered, etc.)
            - 100
                - basic information
            - 200
                - success
            - 300
                - redirects
            - 400
                - CLIENT error
            - 500
                - SERVER error (this is really bad: developer error)
## JSON intro
With so many coding languages sending information over the web, translation between them can be problematic. Having a unique translation process between each language would be cumbersome to program, so developers get around this by using a common format: Javascript Object Notationn(JSON). JSONs are basically formatted strings, since every coding language has a way of working with strings. This makes it easy to convert data from one language to another over the web. JSONs have a few basic rules
- should follow Javascript naming conventions (camelCase)
- three data types are supported: String, Number, Boolean
- JSONs contain key:value pairs (they are like dictionaries)
```json
{
    "name":"Eric",
    "profession":"instructor",
    "married":true,
    "wives":1,
    "languages":["Java", "Python", "Javascript"]
}
```
## HTTP Requests with Flask
Flask is a microframework for Python that allows you to create web servers and transfer information over the internet. It is what we will be using for this course. All you need to do to create your own web server is download flask with pip, create an instance of it, and run it. (Note: Flask-Cors is needed to avoid CORS issues,)
```cli
pip install flask
```
```python
from flask import Flask, request

import main

app: Flask = Flask(__name__)  # this tells flask where to look for resources (name is a references to the module it resides in)

# to avoid cors issues, you wrap your Flask object in CORS: CORS(app)

count = 0  # we will use this with our count route later on

data_set = {"1": "some data", "2": "more data"}  # we will use this with our query route later on


# the basic anatomy of a flask route is presented in the hello world method below

# @app.route connects this route to the method
# the first argument is the url, you add it to the end of Flasks provided domain name and port
# the second argument sets the verb for the route (can instead do @app.get)
@app.route("/", methods=["GET"])
def hello_world():
    return "Hello World"  # the return MUST BE a string, dict, tuple, response instance, or WSGI callable
    # will focus on strings, dict, and tuples this course


# you can add path paramaters to the route by placing them inside <> brackets
# this is useful for accessing specific information
@app.route("/greeting/<name>", methods=["GET"])
def greeting(name: str):  # make sure to pass them in the method
    return f"Hello {name}!"  # you can then work with them like a regular variable


@app.route("/<num1>/add/<num2>", methods=["GET"])
def addition(num1: str, num2: str):
    result = int(num1) + int(num2)
    return str(result)  # notice we had to cast the int as a string here, else we would have gotten an error


# routes with bodies can not access them in the url: you have to retrieve them from the body of the request
@app.route("/login", methods=["POST"])
def login():
    credentials = request.get_json()  # flask includes this handy method for us: sets our variable to the JSON dictionary values
    # you need to make sure the key values match what is in the json
    username = credentials["username"]
    password = credentials["password"]
    if username == "good" and password == "correct":  # in a real application you would have more robust validation, actually log in, etc
        return "your credentials are good!"
    else:
        return "your credentials are bad!"


# you can also use your routes to affect stored data (think a database) and return data that you want
@app.route("/count", methods=["PATCH"])
def add_count():
    main.count = main.count + 1  # this route adds one to the count variable we set up at the start
    return f"The count is now {main.count}"  # we can then see how many times we have called the route


# you can use query parameters to filter the data you access
@app.get("/data")  # route will look like this: http://domain:port/data?query_param=value
# you can use the & symbol to make multiple query params
def query_database():
    # instead off getting the whole database we will be getting only the part we specify in the query param
    # if no param is provided we get the whole set
    query = request.args["DB"]
    if query == "":  # don't do this in an actual app: use a path param to get all the data
        return data_set
    else:
        return data_set[query]


app.run() # this actually tells Flask to start up your server. Notice we have not created a shut down method, so we need to kill it with our ide for now using the command ctr + c

```

## Webservice
Webservices are simply applications that allow for the transfering of information through the internet. Typically this is done by transfering the data via machine-friendly formatted data (python object is transfered as a JSON to a Java app accross the internet). There are many different architectural styles for creating Webservices, but we will focus on creating RESTful web services.
## REST
A Representational State Transfer (REST) service is a type of web service that is not directly used by humans. Instead, its inputs and outputs are in machine friendly format (think JSON, XML, etc) and this data is worked with instead of the Python/Java/Whatever data the human using the REST service is working with (the Python object, Java object, etc.). What this means is that a RESTful webservice does not send the actual object the user is working with: it sends a representation of the object accross the web. So for instance, if you have a Java and Python application that need to send information to each other, a RESTful web service could handle the communication for them. The Python app could take its data, convert it to JSON formatting, send it to the restful web service, and the service would handle the transfer over the web to the Java application, where it would parse the JSON and create a Java object based upon the data it recieved.
## REST Constraints
there are 7 constraints a RESTful web service must follow to be considered a true REST webservice
1. Client - Server architecture
    - RESTful web services are not complete applications: they do not handle any client logic.
    - with this architecture, feasibly any client-side tech could interact with your server: the data being sent to the client does not HAVE to be specific to any one particular software
2. Stateless
    - RESTful webservices do not keep track of the client: this is handled clientside (no cookies, for example)
3. Cacheable
    - can cache information from the server clientside for optimization
4. Uniform Interface
    - This is a standard web service convention
        - resrouces handeled by a RESTful web service should be identifiable by a Uniform Resource Identifier (URI). For instance, if you are dealing with customers, their identifier in the path should be "customer"
        - you then use specific verbs with your URIs to determine what will actually happen
            - GET/customer/1 should get the information for customer 1
            - the meaning of the URI should be clear even without a description
        - Hypermedia as the Engine of Application State (HATEOAS) should also be followed
            - basically, instead of sending constant http requests to the server to navigate, clients should be able to use links (think hyperlinks) to navigate
5. Layered System
    - RESTful web services should be able to call other services
    - this is not something the client needs to be aware of
        - you might implement a layer of security that the RESTful web service has to pass the client request through before it hits your database, or the request could be rerouted somewhere, etc
6. (optional) Code on Demand
    - RESTful web services can return executable code (like Javascript) that the client web browser can execute
    - this is not a normal practice, and therefor it is optional

## HTTP (Creating HTTP handlers is covered in Flask and Javalin sections)
HTTP Status codes in-depth:
- 100
    - Continue status code (it means everything is fine and the HTTP request should continue)
- 200
    - The general success code
    - 201 is for successfully creating an object/resource
    - 204 is success but there is no information to return to the requester
- 300
    - redirect
        - not common in RESTful services
- 400
    - Client error (data was entered incorrectly, login failed, tried to divide by zero, etc)
    - 401 unauthorized
    - 403 forbidden
    - 404 not found
    - 405 method not permitted for this endpoint
    - 422 Unprocessable
- 500
    - Server error
    - the server is unable to handle the request because something is either not working properly or has not yet been implemented. These are developer mistakes, not client mistakes
    - You really do not want 500 errors
HTTP Verbs
- GET
    - Used to retrive infromation
    - GET requests do not have a body
- PUT
    - Use PUT when you are replacing an object or some sort of data
- POST
    - Use POST when creating an object or some kind of data
- DELETE
    - Use DELETE when removing data
- PATCH
    - Use PATCH when you are updating or editing an object or data



