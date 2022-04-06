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

// anonymous functions are similar to regular functions
let myFunc = function(){
    console.log("this works as a function")
}
myFunc() // this will print the message to the console

// there are also self-invoking functions, or Immediately Invoked Function Expressions. They run after they are defined
(function(){
    console.log("runs right away");
})();

// callback functoins pass a function as an argument
function callbackFunc(number){
    return number + 5
}
function myFunc(num, callbackFunc){
    console.log(callbackFunc(num))
}
myFunc(3, callbackFunc) // will return 8, because myFunc passes the number 3 into the callbackFunc function which adds the number with 5
// this also works with anonymous functions

// a closure is a function that can access variables and arguments in its outer function, even after a function return
function greeting(){
    let message = "Hello!"

    function sayHello(){
        console.log(message)
    }

    return sayHello()
}
greeting() // prints Hello! to the console

```
## arrow functions
- another way to write functions
```javascript
let func = () => "Hello world!"
let sum = (numOne, numTwo) => let result = numOne + numTwo
```
## Arrow Notation
- similar to creating regular functions
- key difference is arrow functions don't utilize "this" or "super" keyword
- should not be used as methods (property of object)
```javascript
// param => expression. need {} if there are multiple lines
a => a + 100 // returns a plus 100
a =>{
    num = 100
    return a + num
}
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
## bubbling, capturing
- take the following code:
```javascript
<div onClick="alert('Bubbling: ' + this.tagName)">
    <p onClick="alert('Bubbling: ' + this.tagName)">
        <a onClick="alert('Bubbling: ' + this.tagName)">
            click me
        </a>
    </p>
</div>
```
- upon clicking the a element, the alerts will appear in the following order:
    - a
    - p
    - div
- the events "bubble up"
- use event.stopPropagation() to end the bubbling early
- take the following code:
```html
<div id="wrap">DIV
    <p class="hint">P<br>
        <a href="#">Click Me!!</a>
    </p>
</div>
<script>
    function showTagName {
        alert("Capturing: "+ this.tagName);
    }
    var elems = document.querySelectorAll("div, p, a");
    for(let elem of elems) {
        elem.addEventListener("click", showTagName, true);
    }
</script>
```
- clicking on the a element will produce the following result
    - div
    - p
    - a
- the code will scan the topmost element and work its way down, this is called capturing
- the event target is the element that has generated the event in the DOM. use event.target to acces the target element
- to prevent bubling and all other handlers, use event.stopImmediatePropagation()
## selecting elements from the DOM
```javascript
document.getElementByID("id") // selects a single element with the given id
document.getElementByClassName("class")// returns an array-like object of all elements which have the class
document.getElementByTagname("tag")// returns an array-like object of all elements with the given tag
document.querySelector("CSS selector","CSS selector two")// selects element that matches specified css selectors. if multiple finds the first instance
document.querySelectorAll("CSS selector","CSS selector two") // finds all elements that match CSS selectors 
```
## DOM Manipulation
```javascript
// this creates a new element and adds it to the DOM tree
var element = document.createElement('div')
element.innerHTML = '<p>Hellow World!</p>'
document.body.appendChild(element); // this actually adds the tag to the document

// this removes an element from the DOM tree and inserts something new in its place
var element = document.getElementByTagname('div')
var newElement = document.createElement('p')
newElement.innerHTML = '<b>This will replace the div element</b>'
element.parentNode.replaceChild(newElement, element)

// this removes an element from the DOM tree
var element = document.getElementByClassName("class")
element.parentNode.removeChild(element) 

// this adds nodes to the end of the list of child nodes of a specified parent node.
// <ul id="animals></ul>
function createAnimalList(name) {
            let li = document.createElement('li');
            li.textContent = name;
            return li;
        }
        // get the ul #animals
        const list = document.querySelector('#animals');
        // add animals to the list
        list.appendChild(createAnimalList('Lion'));
        list.appendChild(createAnimalList('Tiger'));
        list.appendChild(createAnimalList('Wolf'));

// this inserts a node before another node as a child node of a parent node.
//     <ul id="animal">
//     <li>Lion</li>
//     <li>Tigerr</li>
//     </ul>
let animal = document.getElementById('animal'); 
// create a new li node
let li = document.createElement('li');
li.textContent = 'Wolf';
// insert a new node before the first list item
animal.insertBefore(li, animal.firstElementChild);

// to insert "after" a node you have to get a little creative with the insertBefore() method
let animal = document.getElementById('animal');        
// create a new li node
let li = document.createElement('li');
li.textContent = 'Wolf';
// insert a new node before the second list item
animal.insertBefore(li, animal.firstElementChild.nextSibling);

// textContent sets the text inside a node
// <div id = "content">
//     This is div element.
// </div>
// Getting a text content
let content = document.getElementById('content');
alert("Getting a text content inside div element: " +  content.textContent);
//setting a text content
content.textContent = 'New text content in the div element';

// textContent gets the inner text, innerHTML returns text and HTML
// <div id="myBdy">
// <p id = "para">This is Paragraph.</p>
// <button onclick="myFunction()"  >Try it</button>
// <p id="demo"></p>
// </div>
function myFunction() {
// get HTML of Element
var x = document.getElementById("para").innerHTML;
document.getElementById("demo").innerHTML = x;  
}
// You can understand the difference between innerHTML and textContent property clearly from the output of the
// below two alert boxes
alert ("textcontent property:" + document.getElementById("myBdy").textContent);
alert ("innerHTML property:" + document.getElementById("myBdy").innerHTML);

// cloneNode clones the element it is called on. if you add true to the parameter you clone the element and 
// all child elements
// <ul id="animal">
// <li>Lion</li>
// <li>Tiger</li>
// <li>Wolf</li>
// </ul>        
let list = document.querySelector('#animal');
let clonedList = list.cloneNode(true);
clonedList.id = 'cloned animal';
document.body.appendChild(clonedList);

// managing attributes
getAttribute(attribute_name) Used to get the value of an attribute on a specified element
setAttribute(attribute_name, attribute_value) Used to set a value of an attribute on a specified element,
removeAttribute(attribute_name) Used to remove an attribute with a specified name from an element
hasAttribute(attribute_name) Used to check an element has a specified attribute or not.
```
Traversing the DOM
```javascript
document.documentElement // refers to node in the html tag
document.head // refers to node in the head tag
document.body // refers to node in the body tag

// use parentNode and parentElement to access nodes that are one level up in the DOM tree
// <div id="main">
//     <p id="para">This is a note!</p>
// </div>
let element = document.querySelector('#para');
document.write(element.parentNode+ "<br>"); // outputs: [object HTMLDivElement]

// child nodes are those that are a level below in the DOM tree.
childnode // returns list of child nodes
firstChild // returns first child node
lastChild // returns last child node
// <div id="myDiv">
//     <p>This is a paragraph - first child</p>
//     <div> this is a div elemt - last child</div> 
// </div>
let elmt = document.querySelector('#myDiv');
document.write("<br> Child nodes of div element: <br>");
for (let i = 0; i < elmt.childNodes.length; i++) {
        document.write(elmt.childNodes[i]  + "<br>");
        }   
document.write("<br> First child of div element: <br>" +elmt.firstChild) ; 
document.write("<br> Last child of div element: <br>" +elmt.lastChild) ;

// siblings are children of the same parent node
previousElementSibling // gives access to the node before the specified node
nextElementSibling // gives access to the node that comes after the specified node
// <ul >
//     <li>list item 1</li>
//     <li class="list">list item 2</li>
//     <li>list item 3</li>
// </ul>
const secondListItem = document.querySelector('.list');       
document.write(secondListItem.previousElementSibling.textContent) ;  // outputs:  "list item 1"
document.write(secondListItem.nextElementSibling.textContent);   //outputs: "list item 3"  
```
Event Object
- all events in javascript have the Event object as a prototype, so they share some properties.
- curated list of properties:
    - bubbles: a boolean value. A true value indicates that the event is bubbling, false indicates that it is capturing. See Bubbling and Capturing
    - currentTarget: a reference to the DOM element whose event listener triggered this specific event. This is different from the event that initially triggered the event as a single event can trigger multiple event listeners through propagation.
    - preventDefault(): Cancels the event, preventing the default action that would normally occur.
    - stopPropagation(): Prevents the event from propagating further.
    - target: a reference to the DOM element which triggered the event.
    - timeStamp: the time of the event in milliseconds
    - type: the type of the triggered event
Events and Listeners
```javascript
element.addEventListener(event, functionHere(), useCapture)
// event is the name of the event used
// functionHere() the name of the function run when the event occurs
// useCapture is an optional boolean value. If true, event handled in capture phase, else bubble phase
element.removeEventListener(event, functionHere(), useCapture)
```
Template Literals
```javascript
// utilizes back-ticks `. these allow for string interpolation and multiline string
let name = "Eric"
let greeting = `hello ${name}`
let multiLineString = `this is a multi
line string`
```