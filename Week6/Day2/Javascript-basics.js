console.log("This comes from my linked JS file")

// Javascript primitive data types
// string
// number
// bigInt
// boolean
// null
// undefined
// symbol

myString = "This is a string";
myNumber = 10;

// Javascript Scopes
// Global scope: no keyword
// Function scope: var keyword
console.log(myFunctionScopeVariable)
var myFunctionScopeVariable = "this is function scope"
console.log(myFunctionScopeVariable)

// Block Scope: let and const

const myVariable = 10;
// myVariable = 11; this will cause a TypeError because you can't reassing a constant value

let myNewVariable = "this is a string";
myNewVariable = 10;
console.log(myNewVariable);

// Scopes take-away: make const and let your bread and butter when working with JS variables, shy away from var

// Truthy/Falsey

console.log("5" == 5); // this is going to return as true, because JS is going to coerce the data types to try and compare them
console.log("5" === 5); // use the "strict equality operator" when you need to check if the data types are the same first

// falsey values: if provided in a logical check, the check will return a False value
const emptyString = "";
let undefinedVariable;
let nullVariable = null;
let notANumberVariable = NaN;
const zero = 0;

if(zero){
    console.log("I got a true result");
} else {
    console.log("I got a false response");
}

// truthy values: anything not a falsey value is considered a truthy value

if(5){ // this will be considered a True result
    console.log("I got a true result");
} else {
    console.log("I got a false response");
}