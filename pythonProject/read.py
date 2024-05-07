from connect import *  # import everything from the connect.py file
 
def read():
    try:
        cursor.execute("SELECT * FROM tblfilms") 
        row = cursor.fetchall() # obtain all the records and they are stored in the row variable
        for aRecord in row:
            print(aRecord)    
    except sql.OperationalError as e:
        print(f"Records not found: {e}")
 
if __name__ == "__main__":
    read()