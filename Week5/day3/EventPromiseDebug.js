1. 
document.getElementByid('btn').addEventlistener('click', function() {
    alert('Button clicked!');
  });
  
  2. 
  var myPromise = new Promisse((resolve, reject) => {
    resolve('Success!');
  });
  
  3. 
  setTimeout( ()=> {
    console.log("Timeout completed");
  }, 1000);
  
  4. 
  myPromise.then(response => {
    console.log(response);
  }).catch((error) => {
    console.log('Error: ', error);
  });
  
  5. 
  document.querySelecter('#myElement').innerText = 'New Content';
  
  6. 
  let count = 0;
  array.forEach(item => {
    consol.log(count += item);
  });
  
  7. 
  document.getElementByid('btn').addEventListner('click', myFunction);
  function myFunction() {
    alert('Button clicked!');
  }
  
  8. 
  new Promise((resolve, reject) => {
    if (true) {
      resolve('Done!');
    } else {
      reject('Failed!');
    }
  });
  
  9. setTimeout(function() {
    console.log('Delayed message');
  }, 2000;
  
  10. document.getElementByID('anotherBtn').addEventListener('click', function) {
    console.log('Another button clicked');
  });
  
  11. myPromise.then(success => {
    console.log('Success:', success);
  }).catch(error => {
    console.log('Error:', err);
  });
  
  12. document.querySelector('.myClass').addeventListener('mouseover', function() {
    console.log('Mouse over');
  });
  
  13. const promiseTest = new Promise((resolv, reject) => {
    reject('This was rejected');
  }).catch(error => {
    console.log(error);
  });
  
  14. let sum = 0;
  [1, 2, 3].forEach((num) => {
    sum =+ num;
  });
  console.log(sum);
  
  15. function callbackExample(callback) {
    callback();
  }
  callbackExample(() => {
    console.log('Callback called');
  };
  
  16. document.querySelector('button').addEventListener('mouseup', e => {
    console.log('Mouse up on button');
  });
  
  17. setTimeout(() => (
    console.log('Missing parenthesis');
  ), 1000);
  
  18. document.getElementByClassName('container').forEach(element => {
    element.style.backgroundColor = 'red';
  });
  
  19. new Promise((resolve, reject) => {
    throw 'Error occurred';
  }).then(result => {
    console.log(result);
  }).cath(error => {
    console.log(error);
  });
  
  20. function loadData(callback) {
    callback;
  }
  loadData(() => console.log('Data loaded'));