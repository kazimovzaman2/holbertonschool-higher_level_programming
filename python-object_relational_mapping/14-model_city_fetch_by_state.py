#!/usr/bin/python3
"""
This script fetches all the states from the database and prints them.
"""

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """
    Main entry point of the script.
    """

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = Session(engine)

    query = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
