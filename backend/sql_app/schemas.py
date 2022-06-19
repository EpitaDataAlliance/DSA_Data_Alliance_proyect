from typing import Optional
from pydantic import BaseModel

import datetime


class PredictionBase(BaseModel):
    params: str
    prediction: int
    datetime: datetime.datetime


class PredictionCreate(PredictionBase):
    pass


class Prediction(PredictionBase):
    id: int
    
    
    class Config:
        orm_mode = True





# class HomeWorkBase(BaseModel):
#     title: str
#     description: Optional[str] = "-"

# class HomeWork(HomeWorkBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     home_works: List[HomeWork] = []

#     class Config:
#         orm_mode = True