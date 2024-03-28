
fetch ('http://jsonplaceholder.typicode.com/users')
.then(response=>response.json())
.then(users=>{
    const userCard = document.getElementById('userCard')

    users.forEach(user=>{
        console.log(user.name)
       const userDatails = document.createElement('div')
       userDatails.classList.add('user-details')
        userDatails.innerHTML = `
        <div > name: ${user.name}</div>
        <div > email: ${user.email}</div>
        `
        userCard.appendChild(userDatails)

    })
})
.catch(error => console.error('error fetching users:', error))
