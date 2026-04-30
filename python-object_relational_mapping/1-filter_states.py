#!/usr/bin/python3
"""
This module provides a script that lists all states with a name starting
with 'N' from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def list_n_states():
    """
    Connects to the database and prints states starting with 'N'
    sorted by their id.
    """
    # Extracting arguments from sys.argv
    u_name = sys.argv[1]
    u_pass = sys.argv[2]
    d_name = sys.argv[3]

    # Connecting to the MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=u_name,
        passwd=u_pass,
        db=d_name
    )

    # Creating a cursor object to execute SQL commands
    cursor = db.cursor()

    # Executing SQL query with a filter for names starting with 'N'
    # The BINARY keyword ensures the search is case-sensitive if needed
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetching all rows from the executed query
    rows = cursor.fetchall()

    # Printing each row in the (id, name) format
    for row in rows:
        print(row)

    # Closing the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Prevent execution when the script is imported
    list_n_states()
