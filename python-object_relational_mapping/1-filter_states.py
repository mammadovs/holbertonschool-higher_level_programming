#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa
starting with the letter N.
"""
import MySQLdb
import sys


def list_n_states():
    """
    Connects to the MySQL database and retrieves states
    starting with 'N', sorted by id.
    """
    # Database connection using command line arguments
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Creating a cursor to execute the query
    cursor = db.cursor()

    # Selecting states starting with 'N'.
    # BINARY is used to ensure it matches 'N' and not 'n'.
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                   "ORDER BY states.id ASC")

    # Fetching and printing the results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Closing cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Ensure the script does not execute when imported
    list_n_states()

