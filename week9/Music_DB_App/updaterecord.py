"Objectives"
"" '' # Import connect module
"" '' # Create a function to update record(s) in a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement

from connect import *
 
def update():
        idField = input("Enter the ID of the record to be updated: ") # int()
 
        fieldName = input("Enter the field to be updated (Title, Artist, Genre): ").title() # capitalise() in JS
        print(fieldName)
        newValue = input(f"Enter the value for {fieldName}: ") # python string output
        #print the value to check  
 
        # newValue = "'"+newValue+"'"
 
        try:
            cursor.execute(f"UPDATE songs SET {fieldName} = '{newValue}' WHERE SongID = {idField}")
            conn.commit()
            print(f"Record {idField} has been updated")
               
 
        except sql.OperationalError as e:  
            conn.rollback()
            print(f"Record not updated: {e}")
 
 
if __name__ == "__main__":
     update()