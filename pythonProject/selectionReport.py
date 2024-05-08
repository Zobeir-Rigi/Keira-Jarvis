from connect import *

def printFilmsByGenre():
    genre = input("Enter the genre to search: ").title()

    try:
        cursor.execute("SELECT * FROM tblFilms WHERE genre=?", (genre,))
        films = cursor.fetchall()
        if films:
            print(f"Films in the {genre} genre:")
            for film in films:
                print(film)
        else:
            print(f"No films found in the {genre} genre.")
    except sql.OperationalError as e:
        print(f"Error: {e}")

def printFilmByYear():
    movieYear = int(input("Enter the year which movie released: "))
    try:
        cursor.execute("SELECT * FROM tblFilms WHERE yearReleased = ?", (movieYear,))
        films = cursor.fetchall()
        if films:
            print(f"Movies released in {movieYear}:")
            for afilm in films:
                print(afilm)
        else:
            print(f"No movies found released in {movieYear}")
    except sql.OperationalError as e:
        print(f"Error: {e}")

def printFilmByRating():
    movieRating = input("Enter the rating of the movie: ").title()
    try:
        cursor.execute("SELECT * FROM tblFilms WHERE rating = ?", (movieRating,))
        filmsByRate = cursor.fetchall()
        if filmsByRate:
            print(f"Movies released in {movieRating}:")
            for film in filmsByRate:
                print(film)
        else:
            print(f"No movies found released in {movieRating}")
    except sql.OperationalError as e:
        print(f"Error: {e}")

def printByDuration():
    movieDuration = int(input("Enter the duration of the movie: "))
    try:
        cursor.execute("SELECT * FROM tblFilms WHERE duration = ?", (movieDuration,))
        filmsDuration = cursor.fetchall()
        if filmsDuration:
            print(f"Movies released in {movieDuration}:")
            for hours in filmsDuration:
                print(hours)
        else:
            print(f"No movies found released in {movieDuration}")
    except sql.OperationalError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    printFilmsByGenre()
    printFilmByYear()
    printFilmByRating()
    printByDuration()

