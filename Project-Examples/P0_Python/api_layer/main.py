"""This module contains the code for my api"""

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