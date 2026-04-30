#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def list_n_states():
    """
    Connects to the database and fetches states starting with 'N'.
    """
    # Arguments: 1: username, 2: password, 3: database name
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    
    # Using format to include the 'N%' filter
    # Sorting by states.id ASC
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        # Printing only if name starts with 'N' (additional check)
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    # Ensure script only runs if exactly 3 arguments are provided
    if len(sys.argv) == 4:
        list_n_states()
