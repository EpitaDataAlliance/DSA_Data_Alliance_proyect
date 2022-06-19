from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from DB import SessionLocal
import models
from typing import List

app = FastAPI()

class Item(BaseModel):  # serializer
    id: int
    battery_power: float
    blue: float
    clock_speed: float
    dual_sim: float
    fc: float
    four_g: float
    int_memory: float
    m_dep: float
    mobile_wt: float
    n_cores: float
    pc: float
    px_height: float
    px_width: float
    ram: float
    sc_h: float
    sc_w: float
    talk_time: float
    three_g: float
    touch_screen: float
    wifi: float

    class Config:
        orm_mode = True


db = SessionLocal()

@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    items = db.query(models.Item).all()

    return items

@app.post('/items', response_model=Item,
          status_code=status.HTTP_201_CREATED)
def create_an_item(item: Item):
    db_item = db.query(models.Item).filter(models.Item.id == item.id).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item already exists")

    new_item = models.Item(
        battery_power=item.battery_power,
        blue=item.blue,
        clock_speed=item.clock_speed,
        dual_sim=item.dual_sim,
        fc=item.fc,
        four_g=item.four_g,
        int_memory=item.int_memory,
        m_dep=item.m_dep,
        mobile_wt=item.mobile_wt,
        n_cores=item.n_cores,
        pc=item.pc,
        px_height=item.px_height,
        px_width=item.px_width,
        ram=item.ram,
        sc_h=item.sc_h,
        sc_w=item.sc_w,
        talk_time=item.talk_time,
        three_g=item.three_g,
        touch_screen=item.touch_screen,
        wifi=item.wifi
    )

    db.add(new_item)
    db.commit()

    return new_item