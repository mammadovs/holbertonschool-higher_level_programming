#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
using the relationship attribute.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco")

    # Link them using the relationship
    new_state.cities.append(new_city)

    # Adding the state will automatically add the city due to the relationship
    session.add(new_state)
    session.commit()

    session.close()
