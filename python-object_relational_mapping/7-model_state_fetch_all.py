#!/usr/bin/python3
"""
This module lists all State objects from the database hbtn_0e_6_usa.
It uses SQLAlchemy to perform the query.
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

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all State objects, sorted by id
    states = session.query(State).order_by(State.id).all()

    # Print each state in the format: id: name
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
