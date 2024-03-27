const numbers = [1,2,3,4,5]

const displayNambers = () => {
    let i = 0
    numbers.forEach( num => {

        setTimeout( () => {  console.log(num) }, i * 1000) 
          i++
          })
    }

displayNambers()

// const numbers = [1, 2, 3, 4, 5];

// const displayNumbers = () => {
//     let i = 0;
//     numbers.forEach(num => {
//         setTimeout(() => {
//             console.log(num);
//         }, i * 1000);
//         i++;
//     });
// };

// displayNumbers();
