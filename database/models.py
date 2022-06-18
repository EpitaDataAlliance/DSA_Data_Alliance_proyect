import datetime as dt
from sqlalchemy import String, Integer, Column, Text, Float
from database import Base

class Item(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key = True, autoincrement=True)
    battery_power = Column(Float)
    blue = Column(Float)
    clock_speed = Column(Float)
    dual_sim = Column(Float)
    fc = Column(Float)
    four_g = Column(Float)
    int_memory = Column(Float)
    m_dep = Column(Float)
    mobile_wt = Column(Float)
    n_cores = Column(Float)
    pc = Column(Float)
    px_height = Column(Float)
    px_width = Column(Float)
    ram = Column(Float)
    sc_h = Column(Float)
    sc_w = Column(Float)
    talk_time = Column(Float)
    three_g = Column(Float)
    touch_screen = Column(Float)
    wifi = Column(Float)
    price_range = Column(String(255), nullable=False)
    
def __repr__(self):
    return f"<Phone ID={self.id} Price range={self.price}>"