import os

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

from config import DATABASE_NAME

database_filename = f'{os.curdir}/{DATABASE_NAME}.db'
engine = create_engine(f'sqlite:///{database_filename}', echo=True)
Base = declarative_base()


def create_all():
	Base.metadata.create_all(engine)


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	name = Column(String)