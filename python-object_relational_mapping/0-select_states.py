#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa.
It connects to a MySQL server and fetches data from the 'states' table.
"""
import MySQLdb
import sys


def list_states():
    """
    Connects to the MySQL database and prints all rows from the states table.
    The results are sorted by states.id in ascending order.
    """
    # Verify if enough arguments are passed
    if len(sys.argv) != 4:
        return

    # Assigning command line arguments to variables
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connecting to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    # Creating a cursor object to interact with the database
    cursor = db.cursor()

    # Executing the SQL query to select all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching all the results from the query
    query_rows = cursor.fetchall()

    # Iterating through the rows and printing each one
    for row in query_rows:
        print(row)

    # Cleaning up by closing the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Ensuring the script does not run when imported
    list_states()
