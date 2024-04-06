// const abortController = new AbortController()
// const signal = abortController.signal

fetch ('https://jsonplaceholder.typicode.com/users')
.then(response=>response.json())
.then(users=>{
    console.log(users[0].email)
    const userCard = document.getElementById('userCard')
    users.forEach(user=>{
        console.log(user.name)
       const userDatails = document.createElement('div')
       userDatails.classList.add('user-details')
        userDatails.innerHTML = `
        <img alt ="userPicture" src = "https://lh3.googleusercontent.com/proxy/ydAXQDqT2RPBYd-7xKLOYqFCBODxKfw4bH4NXkex5bm2mcESn2PSuUQvurMasw5WRgw2EIyqkSazMfZYNjD7eQGYFdw3n2xJ0E7G6CclObeYcKi5aDeLMw">
         <div class='name' > Id : ${user.id}</div>

        <div class='name' > name : ${user.name}</div>
        <div class='name' > username : ${user.username}</div>
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
