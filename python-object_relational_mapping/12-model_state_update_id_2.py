#!/usr/bin/python3
"""
This module changes the name of a State object from the database
hbtn_0e_6_usa. Specifically, it changes the state with id = 2
to "New Mexico".
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Establishing connection to the database
    # Arguments: 1: user, 2: password, 3: database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # If the state exists, update its name and commit the change
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
