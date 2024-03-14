// .shift() .unshift() .slice() .splice() .concat() .join() .map() .filter() .reduce() .forEach() 

let frontend = ['HTML', 'CSS', 'Javascript', 'react.js', 'Next.js', 'Typescript', 'angular']
let shiftedArr = frontend.shift()
console.log(`${shiftedArr} removed from frontend list => ${frontend}`)

let unShiftedArr = frontend.unshift('HTML5')
console.log(`new length is ${unShiftedArr} frontend list => ${frontend}`)

let slicedArr = frontend.slice(3,5)
console.log(`slicedArr is =>${slicedArr}`);

let spliceedArr = frontend.splice(2,0,'Tailwind CSS')
console.log(`slicedArr is ${frontend}`)

let backend = ['Sql', 'Node.js']
let concatedArr = frontend.concat(backend)
console.log(`concatedArr => ${concatedArr}`);

let joinedArr = frontend.join('*')
console.log(`joinedArr => ${joinedArr}`)

let mapedArr = frontend.map(item => console.log(item + " Developer"))

let filteredArr = concatedArr.filter(backend => backend == "Node.js")
console.log(`filteredArr =>${filteredArr}`)

let numbers = [2,5,6]
let reducedArr = numbers.reduce((acc, cur) => acc * cur)
console.log(`reducedArr => ${reducedArr}`)

frontend.forEach(item => console.log(item))

