

let greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Greetings'];
console.log(greetings.length)
for ( let i = 0 ; i < greetings.length ; i++){
    console.log(`${greetings[i]}, Saeid`);
}

greetings.forEach(function (greet){
    console.log(greet)
} )

greetings.forEach(greet => console.log(greet))