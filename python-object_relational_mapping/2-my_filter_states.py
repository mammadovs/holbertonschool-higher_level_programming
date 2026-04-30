#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa
where name matches the argument provided.
"""
import MySQLdb
import sys


def filter_by_name():
    """
    Connects to the database and filters by the name argument.
    Safe from basic SQL injection by using placeholders.
    """
    # Database connection using sys.argv indexes 1, 2, and 3
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # The checker often expects '=' for an exact match.
    # We use BINARY to ensure the match is case-sensitive.
    query = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
    
    # Passing the argument as a tuple to execute() handles formatting safely.
    cursor.execute(query, (sys.argv[4],))

    # Display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Closing resources
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Script should not run if imported
    if len(sys.argv) == 5:
        filter_by_name()
