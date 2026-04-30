#!/usr/bin/python3
"""
This module lists all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
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

    # Query all State objects and their cities relationship
    # Results are sorted by State.id and then City.id
    # The relationship 'cities' handles the retrieval
    states = session.query(State).order_by(State.id).all()

    # Iterate through the states and their nested cities
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda c: c.id):
            print("    {}: {}".format(city.id, city.name))

    # Close the session
    session.close()
