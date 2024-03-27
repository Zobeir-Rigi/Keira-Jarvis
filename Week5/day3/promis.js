const url = "https://api.tvmaze.com/shows/82/episodes";

// Creating a Promise to fetch data
let fetchData = new Promise((resolve, reject) => {
    // Making an API request
    fetch(url)
        .then(response => response.json())
        .then(data => resolve(data)) 
        .catch(error => reject(error)); 
});

fetchData.then((data) => {
    console.log("Data fetched successfully:", data);
});
