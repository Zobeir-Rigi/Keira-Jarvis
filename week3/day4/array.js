let arr = ['Apple', 'Banana',true, 1 ]
console.log(arr[1])
arr.push(12.1, 'orange')
console.log("add to the end of arr", arr)
arr.unshift('start')
console.log("Added to the begining of arr", arr)
arr.pop()
console.log("removed last item",arr)
arr.splice(1,0,'KIWI')
console.log("Added kiwi to the index 1 of our arr", arr)