#!/usr/bin/python3
"""script that lists all State objects from the database"""
import sys
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = session()
    for instance in session.quary(state).order_by(state.id).all():
        print('{0}: {1}'.format(instance.id, instance.name))
    session.close()

