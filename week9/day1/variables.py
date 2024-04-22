"Objectives"
"" '' #Variables and Variable naming convention
"" '' #Use meaningful identifiers
"" '' #Determine the need for variables
"" '' #Output data (e.g. print (myVvar))


"" '' # Note: This is what happens when you create a variable in python
"" '' # 1. Creates and int/float/string object (variable)
"" '' # 2. Assign the object the value
"" '' # 3. use or print the object

num1=5; num2=2 ; num3=3
answer1 = num1 + num2
print(answer1)
answer2 = num3 * num2
print(answer2)
answer3 = answer1 + answer2
print(answer3)



"" '' # Task 1: Complete the code below to assign values to the respective variables (replace the place older)
"" '' # In the code below, multiple values(objects) are assigned to multiple variables in a single line respectively
"" '' # That is the variables: 1. name 2. address 3.interest

name, address, interest = "Zobeir", "Camden", "software engineering"
print(name, address, interest)



"" '' # Task 2 (Chained assignment): Complete the code below to assign values to the respective variables (replace the place older)
"" '' # In the code below, multiple variables are assigned to the same variable.
"" '' # That is the variables: 1. first_child 2. second_child 3.third_child all assigned to "your name"

first_child = second_child = third_child = "your name"
print(
    "I am the first child",
    first_child,
    "\nI am the second child",
    second_child,
    "\nI am the third child",
    third_child,
)

"" '' # You have now seen the how to assign multiple values(objects) to multiple variables and chained assignment.
"" '' # In your own words, can you explain the difference between the two assignments(multiple variables and chained assignment.)?"
"" '' # we use same value for different varilble


"" '' # Object references 2
"" '' # Rather than creating a new object when num4 = num1 code is executed, it creates a symbolic name/reference, 
"" '' # and num4 now point to the object with a value of 10 same as num1

"" '' # multiple references to the same object
num4 = num1  # multiple references to the same object

"" '' # The use of the id function to return the identify of an object
print(id(num1))  # id returns the identify of an object
print(id(num4))

"" '' # Task 2: Explain why the identity of the two objects/variables below when num1 = 10 and num4 = "10" are not the same
num1 = 10
num4 = "10"
print(id(num1))
print(id(num4))







