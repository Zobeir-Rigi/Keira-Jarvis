from connect import *
from addFilm import *
from deleteFilm import *
from read import *
from updateFilm import *
from selectionReport import *

def optionMenu():
    while True:
        print("\nOptions Menu:")
        print("1. Add a record")
        print("2. Delete a record")
        print("3. Amend a record")
        print("4. Print all records")
        print("5. Report")
        print("6. Exit")
        
        option = input("Enter your choice: ")
        
        if option == "1":
         insertFilm()      
        elif option == "2":
                 delete()
        elif option == "3":
                 update()
        elif option == "4":
                 read()
        elif option == "5":
            printFilmsByGenre()
        elif option == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
if __name__ == "__main__":
    optionMenu()
