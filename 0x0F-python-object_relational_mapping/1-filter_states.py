import MySQLdb
import sys

def list_states_starting_with_n(username, password, database_name):
    """
    Connects to the MySQL database and lists all states with names starting with 'N' from the 'states' table.

    Parameters:
        username (str): MySQL username.
        password (str): Password for the MySQL user.
        database_name (str): Name of the MySQL database.

    Returns:
        None
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
        cursor = db.cursor()

        # Execute SQL query
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

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

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1:]
    list_states_starting_with_n(username, password, database_name)
