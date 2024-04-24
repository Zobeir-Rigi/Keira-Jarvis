"Modify/Make"

# Note: files for the tasks below are in the 

# To Do:
searchStr = "Python is a great programming language"
findChar = input("Enter character to search for: ")

if findChar not in searchStr:  # opposite of the in operator is the 'not in'
    print(f"not Found {findChar}")
else:
    print(f"Found {findChar}")

# Task 5: Replace the in operator above with the 'not in' operator, run the code then explore the output in the terminal "


# Task 6: use if and 'in' operator to find a character in your name"

name = "Add your full name here"  # Add your name in between the speech marks 
findChar = input("Enter character to search for: ")

if findChar in name:
    print(F"found{findChar}")

"Extension and research of using for loop and if statement "

# You have been provided with the vowels in a list data structure and a variable
# called 'name' that is assigned with an empty string.

"Your task is to assign your name to the variable called name and use a for loop and an if statement to:"
"Iterate through the list of vowels to find the vowels in your name"
"          0,   1  ,   2,  3,  4"
counter = 0
vowels = ["a", "e", "i", "o", "u", "j"]  # vowels
name = "Saeid"  # Add your name in between the speech marks 
for char in name :
    if vowels in name :
        counter =counter+1

# Further reading on operators not covered in the bootcamp see links below
"https://www.w3schools.com/python/gloss_python_identity_operators.asp"
"https://www.w3schools.com/python/gloss_python_bitwise_operators.asp"
