function countDown(number) {
    if (number <= 1){
        console.log("enter a number more than 1")
    }
    for (let i = number; i > 0; i--) {
        console.log(i);
        if (i===1){
            console.log("Blast Off");
        }
    }
}

countDown(4);
