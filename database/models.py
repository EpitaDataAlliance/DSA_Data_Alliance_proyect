import datetime as dt
from sqlalchemy import String, Integer, Column, Text
from database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key = True)
    description = Column(Text)
    price_range = Column(String(255), nullable=False)
    
def __repr__(self):
    return f"<Phone ID={self.id} Price range={self.price}>"