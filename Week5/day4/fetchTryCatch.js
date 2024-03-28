async function fetchData() {
try{
        const response = await fetch('http://jsonplaceholder.typicode.com/users')
        if (!response){
            throw new Error('fetch unsuc')
        }else {
            const data = await response.json()
            console.log(data)
        }
}catch{
    console.log("err")
}
}
fetchData()