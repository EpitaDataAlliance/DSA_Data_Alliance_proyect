from typing import Optional
from pydantic import BaseModel

import datetime


class PredictionBase(BaseModel):
    # params: str
    prediction: int
    datetime: datetime.datetime
    numcores: int
    intmemory: int
    ram: int
    pc: int


class PredictionCreate(PredictionBase):
    pass


class Prediction(PredictionBase):
    id: int
    
    class Config:
        orm_mode = True
