from connect import *

def insertFilm():
    myFilm = []
    
    title = input("Enter the Movie name: ")
    yearReleased = int(input ("Enter the year the movie was released: "))
    rating = float(input ("Enter the rating of the movie: "))
    duration = input("Enter the duration of the movie: ")
    genre = input ("Enter the genre of movie: ")

    myFilm.append(title)
    myFilm.append(yearReleased)
    myFilm.append(rating)
    myFilm.append(duration)
    myFilm.append(genre)

    # myFilm = myFilm + [title, yearReleased, rating, duration, genre]
    
    try:
        cursor.execute("INSERT INTO tblFilms (title, yearReleased, rating, duration, genre ) VALUES(?,?,?,?,?)", myFilm)
        conn.commit() 
        print(f"{title} added to the tblFilms table")
    except sql.OperationalError as e:
        conn.rollback()
        print(f"Record not added: {e}")

if __name__== "__main__":
        insertFilm()