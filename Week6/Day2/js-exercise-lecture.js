let myObject = {
    "myFunc":myFunction
}

function myFunction(name){
    return `Hello ${name}!`
}

console.log(
    myObject.myFunc("Alex")
)

// I want to check that myObject actually has a key called myFunc and that it has an associated truthy value

if(myObject["myFunc"]){
    console.log("Yes, myObject does have a key called myFunc with an associated truthy value");
} else {
    console.log("No, myObject does not have a key called myFunc with an associated truthy value")
}