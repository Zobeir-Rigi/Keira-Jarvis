const numbers = [1,2,3,4,5]

const pickRandom = () => {
    const randomIndex = Math.floor(Math.random() * numbers.length);
    return numbers[randomIndex];

};
setInterval(() => {
    const randomNum = pickRandom();
    console.log(randomNum);
}, 1000);