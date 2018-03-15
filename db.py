import os
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

TOP_LEVEL_DIR = os.path.abspath(os.curdir)
engine = create_engine('sqlite:///' + TOP_LEVEL_DIR + '/sqlite.db', echo=True)
Base = declarative_base()

class vids(Base):
    __tablename__ = "vids"
    id = Column(Integer, primary_key=True)
    v_title = Column(String)
    v_id = Column(String)
    v_date = Column(String)

    def __init__(self, v_title, v_id, v_date):
        self.v_title = v_title
        self.v_id = v_id
        self.v_date = v_date

Base.metadata.create_all(engine)
