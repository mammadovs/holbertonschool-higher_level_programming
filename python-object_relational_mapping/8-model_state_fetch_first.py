#!/usr/bin/python3
"""
This module prints the first State object from the database hbtn_0e_6_usa.
It uses SQLAlchemy to query the first record based on states.id.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create the engine to connect to the MySQL server
    # Arguments: 1: user, 2: password, 3: database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object sorted by id
    # .first() is efficient as it doesn't fetch the entire table
    first_state = session.query(State).order_by(State.id).first()

    # Check if the table is empty and display results
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
