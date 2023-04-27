from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from db.base import Base

from models.vaikas import Vaikas
from models.tevas import Tevas


engine = create_engine("sqlite:///test.db")
Base.metadata.create_all(engine, checkfirst=True)
