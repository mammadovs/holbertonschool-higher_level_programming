#!/usr/bin/python3
"""
This module takes a state name as an argument and lists all cities
of that state from the database hbtn_0e_4_usa.
Safe from SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connecting to the database using command line arguments
    # sys.argv[1]: user, [2]: passwd, [3]: db, [4]: state name
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # We use a JOIN to find cities belonging to the state name provided.
    # The %s placeholder and the tuple (sys.argv[4],) prevent SQL injection.
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = BINARY %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (sys.argv[4],))

    # Fetching all results
    rows = cursor.fetchall()

    # The requirement usually asks for names separated by commas
    # or displayed as a list of names.
    # We use a list comprehension and join for the specific format.
    print(", ".join([row[0] for row in rows]))

    # Closing resources
    cursor.close()
    db.close()
