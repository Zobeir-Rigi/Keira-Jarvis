"Objectives"
"" '' # Import connect module
"" '' # Create a function to add record(s) to a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

from connect import *
 
def insertSong():
    #create an empty list
    songs=[]
 
    #obtain values from the user
    title = input("Enter Song Title: ")
    artist = input("Enter Song Artist: ")
    genre = input("Enter Song Genre: ")
 
    #append data to the list "songs"
    songs.append(title)
    songs.append(artist)
    songs.append(genre)
 
    # songs = songs + [title, artist, genre]
 
    try:
        cursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES(?,?,?)", songs)
        conn.commit() # makes the change permanent
        print(f"{title} added to the songs table")
    except sql.OperationalError as e:
        conn.rollback()
        print(f"Record not added: {e}")
 
if __name__ == "__main__":    
    insertSong()
