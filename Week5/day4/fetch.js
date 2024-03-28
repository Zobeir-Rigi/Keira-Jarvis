// const abortController = new AbortController()


// const signal = abortController.signal
fetch ('http://jsonplaceholder.typicode.com/users')
.then(response=>response.json())
.then(users=>{
    const userCard = document.getElementById('userCard')
    users.forEach(user=>{
        console.log(user.name)
       const userDatails = document.createElement('div')
       userDatails.classList.add('user-details')
        userDatails.innerHTML = `
        <div class='name' > name : ${user.name}</div>
        <div > email : ${user.email}</div>
        <div > Adderss : ${user.address.city}</div>
        <div > Website : ${user.website}</div>
        `
        userCard.appendChild(userDatails)

    })
})
.catch(error => console.error('error fetching users:', error))
// setTimeout(()=>{
//     abortController.abort()
// },5000)
