from connect import *
 
def update():
        movieId = input("Enter the ID of the movie to be updated: ") 
        print(movieId)
        fieldName = input("Enter the field name to be updated (title, yearReleased, rating, duration, Genre): ").title() # capitalise() in JS
        print(fieldName)
        newValue = input(f"Enter the value for {fieldName}: ")
        print(f"new value of this field is {newValue}")
 
        # newValue = "'"+newValue+"'"
 
        try:
            cursor.execute(f"UPDATE tblFilms SET {fieldName} = '{newValue}' WHERE filmID = {movieId}")
            conn.commit()
            print(f"Record {movieId} has been updated")
               
 
        except sql.OperationalError as e:  
            conn.rollback()
            print(f"Record not updated: {e}")
 
 
if __name__ == "__main__":
     update()