import os

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_NAME

engine = create_engine(f'sqlite:///{os.curdir}/{DATABASE_NAME}.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


def create_all():
	Base.metadata.create_all(engine)


class User(Base):
	__tablename__ = "users"

	id = Column(String, primary_key=True)
	name = Column(String)