from selectionReport import *
from read import *

def reportOptionMenu():
    while(True):
        print("\nOptions Menu:")
        print("1. Print details of all films")
        print("2. Print all films of a particular genre")
        print("3. Print all films of a particular year")
        print("4. Print all films of a particular rating ")
        print("5. Print all films of a particular Duration ")
        print("6. Exit")
    
        option = input("Enter your choice: ")
        if option == "1" :
           read()
        elif option == "2" :
            printFilmsByGenre()
        elif option == "3" :
            printFilmByYear()
        elif option == "4" :
            printFilmByRating()
        elif option == "5" :
            printByDuration()
        elif option == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
if __name__ == "__main__" :
    reportOptionMenu()
