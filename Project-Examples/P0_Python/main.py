"""This module contains the code for my api"""
from flask import Flask, jsonify, request

from custom_exceptions.bad_team_info import BadTeamInfo
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.team_dao.team_dao_imp import TeamDAOImp
from entities.team_class_information import Team
from service_layer.team_services.team_service_imp import TeamServiceImp

"""
For this application I am going to be making a RESTful web service. REST stands for Representational State Transfer,
and it is a popular way of structuring web application. RESTful webservice inputs (think HTTP Requests) and outputs
(think HTTP Responses) are in a machine friendly format (think JSON). 

There are 6 different constraints to restful web services that help to both guide your development process and that
help you maintain a true RESTful web service.

1. Client-Server architecture
    RESTful web services are not complete applications: they do not handle ANY client logic. Your RESTful web service
    should not handle the creating of the request to your service, but it can handle the response for the request
    that is made.
    
2. Stateless
    RESTful web services do not keep track of clients: any tracking is handled client-side
    
3. Cacheable
    information may be cached client side to speed up operations
    
4. Uniform Interface
    Resources handled by a RESTful web service should easily be identified by the Uniform Resource Identifier
    (URI) that is provided.
    Example uniform URI: GET /customer/2/account/10 should get the information from account 10 belonging to customer
    identified by the number 2
    
5. Layerd System
    RESTful web services should be able to call other RESTful web services
    
6. (optional) Code on Demand
    RESTful web services may return executable code. This is not a common practice, and so it is an optional
    constraint
"""

app: Flask = Flask(__name__)
team_dao = TeamDAOImp()
team_service = TeamServiceImp(team_dao)

"""
To maintain a uniform interface, I will be using the path "/teams" for all request to my application that have to do
with team data. I can use different verbs to determine WHAT I am doing with the team data, and that is how Flask will
know what particular service method needs to be called
"""

@app.route("/teams", methods=["POST"])
def create_team():
    try:
        team_data: dict = request.get_json()
        team = Team(team_data["teamId"], team_data["teamName"], team_data["homeCity"])
        result = team_service.service_create_team(team)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadTeamInfo as e:
        message = {
            "message":str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message":str(e)
        }
        return jsonify(message), 400

@app.route("/teams/<id>", methods=["GET"])
def get_team_by_id(id:str):
    try:
        result: Team = team_service.service_get_team_information_by_id(id)
        result_dictionary = result.convert_to_dictionary()
        return jsonify(result_dictionary), 200

    except BadTeamInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400

app.run()
