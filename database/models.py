from DB import Base
from sqlalchemy import Integer, Float, Column

class Item(Base):
    __tablename__ ='predictions'
    id = Column(Integer, primary_key=True)
    battery_power = Column(Float, nullable=False)
    blue = Column(Float, nullable=False)
    clock_speed = Column(Float, nullable=False)
    dual_sim = Column(Float, nullable=False)
    fc = Column(Float, nullable=False)
    four_g = Column(Float, nullable=False)
    int_memory = Column(Float, nullable=False)
    m_dep = Column(Float, nullable=False)
    mobile_wt = Column(Float, nullable=False)
    n_cores = Column(Float, nullable=False)
    pc = Column(Float, nullable=False)
    px_height = Column(Float, nullable=False)
    px_width = Column(Float, nullable=False)
    ram = Column(Float, nullable=False)
    sc_h = Column(Float, nullable=False)
    sc_w = Column(Float, nullable=False)
    talk_time = Column(Float, nullable=False)
    three_g = Column(Float, nullable=False)
    touch_screen = Column(Float, nullable=False)
    wifi = Column(Float, nullable=False)

def __repr__(self):
     return f"<Item id={self.id} >"
