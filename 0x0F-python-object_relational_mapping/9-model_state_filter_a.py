#!/usr/bin/python3
""" Lists all state objects that contain the letter a from the database """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    """ create session - extract state - print state """
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.like('%a%'))\
            .order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
