from connect import *
 
def delete():
        movieId = input("Enter the ID of the movie to be deleted: ") 
        print(movieId)
        try:
            cursor.execute(f"Delete From tblFilms WHERE filmID = {movieId} ")
            conn.commit()
            print(f"the movie with id number {movieId} has been deleted")
               
        except sql.OperationalError as e:  
            conn.rollback()
            print(f"movie not deleted: {e}")
 
 
if __name__ == "__main__":
     delete()