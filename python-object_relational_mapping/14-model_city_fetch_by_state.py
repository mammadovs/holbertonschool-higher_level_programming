#!/usr/bin/python3
"""
This module prints all City objects from the database hbtn_0e_14_usa.
It joins State and City tables to display state names.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create the engine to connect to the MySQL server
    # Arguments: 1: user, 2: password, 3: database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query both State and City using a join, sorted by City.id
    results = session.query(State, City)\
                     .filter(State.id == City.state_id)\
                     .order_by(City.id).all()

    # Print results in format: <state name>: (<city id>) <city name>
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
