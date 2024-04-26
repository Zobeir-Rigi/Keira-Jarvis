"Objectives"
"" '' # Import connect module
"" '' # Create a function to delete record(s) in a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement

"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

from connect import *
 
def delete():
        idField = input("Enter the ID of the record to be removed: ") # int()  
        try:
            cursor.execute(f"DELETE FROM songs WHERE SongID = {idField}")
            conn.commit()
            print(f"Record {idField} has been deleted")
               
 
        except sql.OperationalError as e:  
            conn.rollback()
            print(f"Record was not found in the database: {e}")
 
 
if __name__ == "__main__":
     delete()