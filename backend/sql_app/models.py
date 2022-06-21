from enum import unique
from sqlalchemy import Column, Integer, DateTime

from .database import Base


class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, index=True)
    prediction = Column(Integer, index=True)
    datetime = Column(DateTime, index=True)
    numcores = Column(Integer)
    intmemory = Column(Integer)
    ram = Column(Integer)
    pc = Column(Integer)
