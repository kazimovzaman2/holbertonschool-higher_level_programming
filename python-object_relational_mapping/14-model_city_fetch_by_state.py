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

    query = session.query(City, State).join(State)

    for c, s in query.all():
        print("{}: ({:d}) {}".format(s.name, c.id, c.name))

    session.commit()
    session.close()
