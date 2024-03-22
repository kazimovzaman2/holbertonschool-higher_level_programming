#!/usr/bin/python3
"""
This script fetches all the states from the database and prints them.
"""

import sys
from model_state import Base, State

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

    louisiana = State(name="Louisiana")

    session.add_all([louisiana])
    session.commit()

    print(louisiana.id)

    session.close()
