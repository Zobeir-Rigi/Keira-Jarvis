// // Create a program that asks the user to guess a number. The program should
// //  repeatedly prompt the user for a guess until they guess the correct number.​

// let hobby = ['cycling', 'reeding', 'smoking', 'swimming', 'listening Music']
// console.log("Hey! so guess what is my fav hobby?")
// let i = 0;
// // while(i < hobby.length){
// //     if 
// // }
const prompt = require('prompt');
const hobbies = ['cycling', 'reading', 'smoking', 'swimming', 'listening to music'];
const secretHobby = "reading";

console.log("Hey! Can you guess what is my favorite hobby?"+'\n'+ "it might be one of these : cycling, reading, smoking, swimming, listening to music");
do {
prompt.get(['guess'], function (err, result) {
    const userGuess = result.guess.toLowerCase();
    
        if(userGuess === secretHobby){
            console.log("congrat");
        }else {
            console.log("wrong, next chance")
        }
        chance--
})} while(chance === 0)
