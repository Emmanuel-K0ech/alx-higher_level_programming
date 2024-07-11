#!/usr/bin/python3
""" Adds state object 'Louisiana' to the database """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, state

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    nw_state = State(name='Louisiana')
    session.add(nw_state)
    state = session.query(State).filter_by(name='Louisiana').first()
    print(str(state.id))
    session.commit()
    session.close()
