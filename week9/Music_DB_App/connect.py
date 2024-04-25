"Objectives"
"" '' # Import sqlite module
"" '' # Understand what is sqlite
"" '' # Create and use a function to create a database file
"" '' # Use try and except to handle error(s)
"" '' # Use the connect function from the sqlite module to create a database file
"" '' # Create a cursor variable from the connect function  

"" '' # Notes:
"" '' #  What is Sqlite
"" '' #  SQLite is a lightweight disk-based database that does not require a separate server process making it easy to integrate into applications
"" '' #  and it uses a variant of the SQL language for database queries to access database. This combination of features makes SQLite a popular 
"" '' #  choice for applications that need a simple and self-contained database solution


import sqlite3 as sql
 
try:
    with sql.connect("week9/Music_DB_App/music.db") as conn:
        cursor = conn.cursor()
except sql.OperationalError as e:
    print(f"Connection Failed!, {e}")
