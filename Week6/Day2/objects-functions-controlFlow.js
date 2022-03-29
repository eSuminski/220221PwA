// objects in JS are essentially key:value pairs

let myObject = {
    "keyOne":1,
    2:"Value Two"
}
console.log(myObject["keyOne"]);
console.log(myObject[2]);

// you can also use the dot operator to access keys in your objects

console.log(myObject.keyOne);

// you can set key:value pairs using the dot operator as well
myObject.keythree = 3;
console.log(myObject["keythree"]);

// you can create functions by using the function keyword, giving it a name, and declaring parameters
function myFunction(){
    return "I got this string from my function";
}

console.log(myFunction());

function mySecondFunction(num1, num2){
    return num1 + num2;
}

console.log(mySecondFunction(1,2));



// we've already seen some control flow in action, but we can take a deeper look

if(true){
    console.log("This message will print because the boolean value returned in the if statement is true")
}

if(false){
    console.log("this is never going to print because the if statement is always getting a false value")
}

let result = true;

if(result){
    console.log("this code block will run");
} else {
    console.log("this only runs if the if statement gets a false boolean value");
}

// if you want to have multiple if statements stringed together you can use else if statements

let checkOne = true;
let checkTwo = true;

if(checkOne){
    console.log("this is the first if block of code");
} else if(checkTwo){
    console.log("this is the second if block of code");
} else{
    console.log("this is the else block of code");
}

// for loops in Javascript work differently from Python: to create a "range" and loop through it you have to take some very different steps
// anatomy of a basic for loop:
// let x = 1 sets the value of the variable that controls the loop
// x <= 5 tells the loop the conditions under which it should continue to run
// x += 1 tells the loop how to change the x variable after each run of the loop
for(let x = 1; x <= 5; x+=1){
    console.log(x);
    // after the console log the value of x is changed according to how we set up the loop
}

// Javascript allows you to create enhanced for loops for both objects and arrays

let obj = {
    keyOne:1,
    keyTwo:2,
    keyThree:3
};

// to easily iterate through an object's key:value pairs you use the in keyword
for(let key in obj){
    console.log(obj[key]);
}

let arr = [1,2,3];

// to easily iterate through an array's stored elements you use the of keyword
for(let element of arr){
    console.log(element);
}