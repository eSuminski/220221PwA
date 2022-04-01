# HTML & CSS
## HTML
overview of html
- Hypertext Markup Language
- markup language for creating web pages and apps
- provides structure and content of webpage
- [great resource](https://developer.mozilla.org/en-US/docs/Web/HTML)

html tags
- tags are used to construct html pages
html document structure
```html
<!-- These are the minimum elements you need to make a webpage  -->
<!DOCTYPE html><!-- default is HTML5, can indicate other versions. Technically not a tag, a declaration -->
<html>
    <head>
        <title>Title goes in here</title>
    </head>
    <body>
        <!-- body of the page goes here -->
    </body>
</html>
```
elements and attributes
- elements are created with tags
- elements can have attributes: these are key/value pairs that provide data about and for the element
inline and block elements
- block elements stack
- inline elements go side by side
    - two inline elements will go side by side when rendered, an inline element next to a block element will instead act like a block element (will not be on the same line as the block element)

## CSS
overview of css
- Cascading Style Sheets
- language used to style html documents
- specifies rules for layout and display in key/value pairs
- rules are declared via selectors and declarations
- selectors are elements or properties
- declarations are properties and their values
```CSS
/* 
    selector: div
    property: color
    value: red
*/
div{
    color:red
}
```
element selectors
- you can determine the css for tags of the same type in an html file
class and id selectors
- you can assign css to a class and add it as an atribute to an element
- you can assign css to an id and add it as an atribute to an element. 
    - Ids should be unique

inline, internal and external stylesheets
- inline is css applied directly to an element within the html tags
```HTML
<p id ="myID" class = "myClass" style = "color:red;text-align:center">my centered red text</p>
```
- internal css is declared between two style tags within the head tags
```HTML
<head>
        <title>Title goes in here</title>
        <style>
            p {
                color:red;
                text-align:center
            }
        </style>
    </head>
```
- external css is a css file that is referenced via a link tag within the head tags
```HTML
<head>
    <title>Title goes in here</title>
    <link rel="stylesheet" href="nameOfStyleSheet.css">
</head>
```
General rule to remember: the closer to the element the styling is declared, the higher its priority for being rendered:
- inline css overrides internal and external css
- internal css overrides external css
- external css is overridden by internal and inline css

# Javascript

## introduction
- most common client-side scripting language
   - with node.js it can be used server-side
- high level
    - memory management is automated
    - garbage collection is handled for the developer
- multi-paradigm
    - can be written functionally
    - can be written for OOP
- interpreted
    - line by line compilation and execution
- case sensitive
    - seperate statemets with ;
        - Javascript will attempt to do this for you if you don't include them, which can sometimes lead to errors 
- can place inside html via script tags
    - can reference it exeternally: 
    ```HTML
    <script src="./script.js"></script>
    ```
## Primitives
- Javascript has 7 primitives:
    - string
    - number
    - bigInt
    - boolean
    - null
    - undefined
    - symbol (es6 datatype, not common)

## variable scopes
- global (no keyword)
- function (var)
    - can be hoisted, not recommended
```html
<!--hoisting is where js moves declarations to the top of the script-->
<p id="demo"></p>

<script>
var x = 5
elem = document.getElementById("demo")
elem.innerHTML = "x is " + x + " and y is " + y //y will equal undefined here
var y = 7
</script>
```
- this works for variables and functions
- functions are hoisted to the top, and then variables
- block (let, const)
    - const is used for constant variables, let for variables that have fluid values
## type coercion
- javascript is loosely typed
    - has aggresive type coercion
    - "+" will convert the result to a string if one of the operands is a string
    - "|,&,!" (or,and,not) will implicitly convert the result to a boolean
        - "<,>,etc" will do the same with numbers
    - == loose equality operator
        - coerces data types and then checks the values
    - === strict equality
        - checks type first, then checks if the values are the same
        - generally the better option of the two
## truthy/falsey
Javascript will implicitly coerce your data into booleans when you make a logical check on it
    - falsey
        - empty string = false
        - undefined variable = false
        - null variable = false
        - Nan = false (always false)
        - 0 = false
    - truthy
        - anything not above = true

## Objects
Objects in Javascript are key:value pairs
```Javascript
let myObject = {
    key:"value",
    1:true,
    func:function myFunction(){return "Hello World!"}
}
```

## functions
```javascript
// basic function
function myFunction(){
    return "return value goes here"
}

// can have parameters
function withParams(num1, num2){
    return num1 + num2
}

// javascript is pass by value: any references passed into function will not be changed
let num1 = 5
let num2 = 7
function passByValue(param1, param2){
    param1 = param1 + 1
    param2 = param2 + 2
    return param1 + param2
}
console.log(num1) // will still show 5
console.log(num2) // will still show 7

// can get around this with objects

let myObj = {"name":"Eric"}
function changeObj(obj){
    obj.name = "Sam"
}
console.log(myObj.name) // this will print Sam, since the argument within the function is referencing the object, which has the name property

// this is still pass by value though, creating a new object with the new value will not change the old object
let myObj = {"name":"Eric"}
function changeObj(obj){
    obj = {"name":"Sam:"}
}
console.log(myObj.name) // this will print Eric, since a new object was created within the function. myObj remained the same
```

## Async/Await
Making requests for data across the web can sometimes lead to long waits, depending on how much data you are requesting. To prevent these requests from stalling the execution of your code (since Javacsript is an interpreted language, meaning the code is compiled and executed line by line) Javascript includes the async and await keywords. By making a function an async function, it makes its return value default to a Promise object. A promise object is a placeholder for the real data you want to recieve, and allows for your code to continue executing while your Promise waits for the intended data. The await keyword is used to stop your function's execution until the Promise object has recieved its data, upon which that data can be used to finish out your function's execution.

## Fetch
The fetch method is used to make HTTP requests via your Javascript. It returns a Promise object by default, so it is a good fit for an async function that makes use of the await keyword. The fetch method takes in two parameters, with the second one being optional
```Javascript
// to make a basic GET request you only need to provide the URL
async function basicGetRequest(){
    let url = "http://Whatever-the-url-is/any/params"
    const response = await fetch(url) // use the await keyword to make your response variable reference the http response
    if(response.status === 200){
        const body = await response.json() // assuming you got a json back, make sure to use await
        console.log(body)
    } else {
        console.log("Request failed: please try again")
    }
}

// to make a non-GET request you also need to provide some configuration details

async function basicPostRequest(){

    let url = "http://Whatever-the-url-is/any/params"
    let bodyContent = {keyOne:1,keyTwo:2} // this can be whatever content you need to send in your http request
    let config = {
        method:"POST",
        headers:{'Content-Type':"application/json"}, // some web servers will reject the request without this header
        body: JSON.stringify(bodyContent) // this turns the Javascript object into a JSON for the http request
    }

    const response = await fetch(url, config)
    if(response.status === 200){
        const body = await response.json() // assuming you got a json back, make sure to use await
        console.log(body)
    } else {
        console.log("Request failed: please try again")
    }
}

```

## Creating/editing html elements/attributes with Javascript
You can use Javascript to create new html elements or edit existing ones using Javascript.

To edit an existing element you first need to create a variable that references the element, then you can manipulate it
```html
<!-- Once the script runs, the paragraph element will have text rendered inside of it -->
<p id="paragraph"></p> 

<script>
    const paragraphElement = document.getElementById("paragraph")
    paragraphElement.textContent = "I added this via Javascript!"
</script>
```

To create a new element you make a variable that references your new element, then you can append it in the page
```html

<ul id="animals">
    <!-- upon the script running, this unordered list will have one list item that says "dog" -->
</ul>

<script>
    const unorderedList = document.getElementById("animals")
    const listItem = document.createElement("li")
    listItem.textContent = "dog"
    listItem.id = "dog"
    unorderedList.appendChild(listItem)
</script>

```