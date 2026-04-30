#!/usr/bin/python3
"""
This module prints the id of the State object with the name
passed as an argument from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # engine connection using format with sys.argv
    # 1: user, 2: password, 3: db, 4: state name to search
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Search for the state. filter() is safe from SQL injection.
    # .first() returns the object or None if not found.
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Display results
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close session
    session.close()
