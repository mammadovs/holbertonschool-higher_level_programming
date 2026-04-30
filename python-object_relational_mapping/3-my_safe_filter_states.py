#!/usr/bin/python3
"""
This module provides a script that safely displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
It is protected against MySQL injection.
"""
import MySQLdb
import sys


def safe_filter_states():
    """
    Connects to the database and searches for a state name securely
    using parameterized queries to prevent SQL injection.
    """
    # Arguments: 1: user, 2: password, 3: db name, 4: state name searched
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # We use %s as a placeholder for the variable.
    # MySQLdb will automatically escape any malicious SQL characters.
    query = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
    
    # The variable must be passed as a tuple: (sys.argv[4],)
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Closing all connections
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Ensure script only runs if 4 arguments are provided
    if len(sys.argv) == 5:
        safe_filter_states()
