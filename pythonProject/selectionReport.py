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

if __name__ == "__main__":
    printFilmsByGenre()
