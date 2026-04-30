#!/usr/bin/python3
"""
This module lists all City objects from the database hbtn_0e_101_usa.
It uses the 'state' relationship to display the state name for each city.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # Create the engine to connect to the MySQL server
    # Arguments: 1: user, 2: password, 3: database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects, joined with their State object
    # sorted by City.id in ascending order
    cities = session.query(City).options(joinedload(City.state))\
                                .order_by(City.id).all()

    # Results must be displayed as: <city id>: <city name> -> <state name>
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
