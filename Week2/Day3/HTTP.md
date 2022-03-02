# HTTP
Hyper Text Transfer Protocal is one of, if not the most, common ways of transfering infortmation across the web. What this system of information transfer does is it takes data in a machine friendly data format and transfers it across the web. There are two main parts to HTTP: the request, and the response. Part of the popularity of HTTP is the guaranteed response to your requests. 

### HTTP Request
All HTTP requests have 5 parts to them:
1. HTTP Version
2. URL
    - the URL is an important part of the HTTP Request, and each part of the URL plays a roll
    - http://www.localhost:5000/greeting?hostile=false
        - http: this part of the url indicates what kind of request I am making
        - www.localhost: this here is the **domain** name: this is where the content we want to interact with is located
        - 5000: this is the **port** where the request is going to be sent: the computer that is hosting the web server that recieves the http request is going to be "listening" on that particular port for our requests
      - /greeting: this is the **path** of my request, these can contain one or more words, seperated by / and they can also contain what is called **path paramters**
      - ?hostile=false: these are our **query** parameters, which are normally used when you want to filter data  
3. Verb
    - the Verb of your HTTP request provides context about what you are trying to accomplish with your HTTP request. There are a few common Verbs that you will be working with
        - GET
        - PUT
        - POST
        - PATCH
        - DELETE
4. Headers
    - headers provide meta data about your HTTP request, and they can sometimes be useful when parsing information from your request
5. Body
    - the body of a request holds all the information for the request. This can be user input data, it can be dates, whatever information you need to pass from the user to your web application is stored in the body of your request
    - GET requests may not have a body

### HTTP Response
1. HTTP Version
2. Headers
3. Body
    - this is where any pertitnent information for the user is stored
4. Status Code
    - this is a quick indication of how the request was handled
    - 100 this is usually just meta data / general information
    - 200 this is the success level
    - 300 this is the reroute level
    - 400 this is the failure level
        - this code is used when the requester makes a bad request
        - this could mean they sent the wrong data, or they made an HTTP requet to the wrong location, etc.
    - 500 this is the failuer level for the web server
        - this is not a failure of the requester, but a failure of the developer.