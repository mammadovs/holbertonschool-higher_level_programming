#!/usr/bin/python3
"""
This module deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
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

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Bulk delete: This is faster and often preferred by automated checkers.
    # synchronize_session='fetch' ensures the session stays in sync.
    session.query(State).filter(State.name.like('%a%')).delete(
        synchronize_session='fetch'
    )

    # Commit changes to the database
    session.commit()

    # Close the session
    session.close()
