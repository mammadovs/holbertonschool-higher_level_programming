#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa
where name matches the argument, safe from MySQL injections.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connecting to the database using arguments from argv
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Creating cursor to execute the query
    cursor = db.cursor()

    # %s is the placeholder for the argument to prevent SQL Injection
    # BINARY ensures the search is case-sensitive
    query = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"

    # Passing argv[4] inside a tuple to the execute method
    cursor.execute(query, (argv[4],))

    # Fetching and printing results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Closing cursor and connection
    cursor.close()
    db.close()
