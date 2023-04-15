from sqlalchemy import Float, String, Column, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_pass = Column(String)


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


class Book(Base):
    __tablename__ = 'books'


    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
    date_published = Column(Date, default=None)



