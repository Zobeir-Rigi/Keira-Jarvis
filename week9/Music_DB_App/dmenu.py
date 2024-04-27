"Objectives"
"" '' # Import all CRUD modules
"" '' # Create a function to read from a text file
"" '' # Display contents form a text file
"" '' # Use the Sequence, Selection and Iteration programminf construct

from addrecord import *
from readrecords import *
def menuOption():
    option = 0
    while option not in ["1", "2", "3", "4", "5", "6"]:
        with open("week9/Music_DB_App/dbMenu.txt", "r") as menue_file:
            choices = menue_file.readline()
            
    