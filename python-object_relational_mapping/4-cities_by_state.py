#!/usr/bin/python3
"""
This module lists all cities from the database hbtn_0e_4_usa.
The script takes 3 arguments: mysql username, password, and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server at localhost, port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor to execute the SQL query
    cursor = db.cursor()

    # Join cities and states to get the state name for each city
    # results are sorted by cities.id in ascending order
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch and print results in the format (city_id, city_name, state_name)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
