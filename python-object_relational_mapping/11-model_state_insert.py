#!/usr/bin/python3
"""
This module adds the State object "Louisiana" to the database
hbtn_0e_6_usa and prints its new id.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup connection to the database
    # Arguments: 1: username, 2: password, 3: database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the new State object
    new_state = State(name="Louisiana")

    # Add the object to the session and commit to save to the database
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print("{}".format(new_state.id))

    # Close the session
    session.close()
