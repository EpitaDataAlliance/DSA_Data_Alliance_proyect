from enum import unique
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, index=True)
    params = Column(String, index=True)
    prediction = Column(Integer, index=True)
    datetime = Column(DateTime, index=True)


# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)

#     predictions = relationship('HomeWork', back_populates='owner')


# class HomeWork(Base):
#     __tablename__ = 'home_works'

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey('users.id'))

#     owner = relationship('User', back_populates='home_works')
