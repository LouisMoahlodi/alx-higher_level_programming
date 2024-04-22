#!/usr/bin/python3

"""
Script to list all states from a MySQL database.

Usage:
    python script.py <username> <password> <database_name>

Arguments:
    <username>: MySQL username with access to the database.
    <password>: Password for the MySQL user.
    <database_name>: Name of the MySQL database containing the 'states' table.

Dependencies:
    - MySQLdb: Python interface for MySQL.
"""

import MySQLdb
import sys


def list_states(username, password, database_name):
    """
    Connects to the MySQL database and lists all states from the states table.

    Parameters:
        username (str): MySQL username.
        password (str): Password for the MySQL user.
        database_name (str): Name of the MySQL database.

    Returns:
        None
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name)
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


if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    # Extract username, password, and database name from command-line arguments
    username, password, database_name = sys.argv[1:]

    # Call the function to list states
    list_states(username, password, database_name)
