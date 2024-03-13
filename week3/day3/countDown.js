let i = 10
while( i >= 1 ){
    console.log(i);
    i--
}

let count = 10 ;
for(;count >= 1 ; count-- ){
    console.log(count);
}

let arrNumbers = [1,2,3,4,5,6,7,8,9,10]
for (let i = arrNumbers.length-1 ; i >= 0 ;i-- ){
    console.log(arrNumbers[i])
}

let numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.reverse()
numbers.forEach(i =>console.log(i))