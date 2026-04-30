#!/usr/bin/python3
"""
This module takes an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


def search_states():
    """
    Connects to the database and filters states by the provided name.
    """
    # Arguments: 1: user, 2: password, 3: db, 4: state name searched
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # Using format to create the SQL query as per instructions.
    # We use BINARY to ensure the search is case-sensitive.
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
             ORDER BY id ASC".format(sys.argv[4])
    
    cursor.execute(query)

    # Fetching and displaying the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Prevent execution on import
    if len(sys.argv) == 5:
        search_states()
