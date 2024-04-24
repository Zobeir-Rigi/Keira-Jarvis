# TASK:
 
# Create a function for a cinema that checks if a customer is eligible to view their film choice.
 
# You will need 3 pieces of information: age, film rating and id (yes or no).
 
# inside the function you will need to filter to the relevant output based on the information provided.
 
# Hint: you will need to use an if/else statement and parameters
def cinema():
    age = int(input("Enter your age: "))
    filmRating = input("Enter the film rating: ")
    id = True

    if filmRating == "18":
        if age >= 18 and id:
            print("Welcome!")
        else:
            print("Sorry")
    else:
        print("Wlcome and Enjoy the Movie")

cinema()

