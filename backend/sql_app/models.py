from enum import unique
from sqlalchemy import Column, Integer, String, DateTime

from .database import Base


class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, index=True)
    # params = Column(String, index=True)
    prediction = Column(Integer, index=True)
    datetime = Column(DateTime, index=True)
