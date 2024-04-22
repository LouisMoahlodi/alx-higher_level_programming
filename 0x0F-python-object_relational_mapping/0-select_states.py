#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
        cursor = db.cursor()

        # Execute SQL query
        cursor.execute("SELECT * FROM states ORDER BY ID ASC")

        # Fetch all rows
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

        # Close cursor and connection 
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)

if  __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password,  database_name = sys.argv[1:]
    list_states(username, password, database_name)
