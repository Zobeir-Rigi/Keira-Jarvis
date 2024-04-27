


var myHeading = document.querySelector('h1');
myHeading.textContnt = 'New Heading Text';

// Debugging Exercise 2: Modifying Styles
// Intended to change the paragraph's text color.
var myParagraph = document.querySelector('p');
myParagaph.style.color = 'red';

// Debugging Exercise 3: Adding an Event Listener
// Intended to show an alert when the heading is clicked.
document.querySelector('h1').addEventListen('click', function() {
  alrt('Heading was clicked!');
});

// Debugging Exercise 4: Creating and Adding an Element
// Intended to add a new paragraph at the end of the body.
var newParagraph = document.createElement('p');
newParagraph.textContet = 'This is a new paragraph.';
document.body.appendChild(newParagraph);

// Debugging Exercise 5: Removing an Element
// Intended to remove a paragraph from the page.
var paragraphToRemove = document.querySelector('p');
document.body.removeChild(paragraphToRmove);

// Debugging Exercise 6: Iterating Over NodeList
// Intended to change the text color of all paragraphs to blue.
var paragraphs = document.querySelectAll('p');
for(var i = 0; i < paragraphs.length; i++) {
  paragraps[i].style.color = 'blue';
}

// Debugging Exercise 7: Capturing User Input
// Intended to log the input field's value when a button is clicked.
document.querySelector('button').addEventListner('click', function() {
  var userInput = document.querySelector('input[type="text"]').value;
  console.log(userInput);
});

// Debugging Exercise 8: Toggling a Class
// Intended to toggle a class for the paragraph.
var myParagraph = document.querySelector('p');
myParagraph.classList.toggle('highlight');

// Debugging Exercise 9: Setting Element Attributes
// Intended to set the src attribute of an img element.
var myImage = document.querySelector('img');
myImage.setAttribute('scr', 'image/path.jpg');

// Debugging Exercise 10: Using `innerHTML` for Content
// Intended to add a list inside a div container.
var myDiv = document.querySelector('.container');
myDiv.innerHTML = '<ul><li>Item 1</li><li>Item 2</li></ul>';

// Note: Each of these examples contains intentional errors for debugging exercises.
