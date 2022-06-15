import pandas as pd
import os
import joblib
import uvicorn

from typing import Optional
from fastapi import FastAPI, File, UploadFile, status

from typing import List
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from database import SessionLocal
import modules

ROOT_DIR = os.path.dirname(os.path.abspath(""))
MODEL_PATH = "../models"
HOST = '0.0.0.0'
PORT = 35998

STYLES = {
    "battery_power": "battery_power",
    "blue": "blue",
    "clock_speed": "clock_speed",
    "dual_sim": "dual_sim",
    "fc": "fc",
    "four_g": "four_g",
    "int_memory": "int_memory",
    "m_dep": "m_dep",
    "mobile_wt": "mobile_wt",
    "n_cores": "n_cores",
    "pc": "pc",
    "px_height": "px_height",
    "px_width": "px_width",
    "ram": "ram",
    "sc_h": "sc_h",
    "sc_w": "sc_w",
    "talk_time": "talk_time",
    "three_g": "three_g",
    "touch_screen": "touch_screen",
    "wifi": "wifi",
}


class Item(BaseModel):
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


class JsonDfItem(BaseModel):
    dataframe1: str
    class Config:
        arbitrary_types_allowed = True

app = FastAPI()

db = SessionLocal()

@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    items=db.quert(models.Item).all()
    
    return items

@app.get('/item/{item_id}')
def get_an_item(item_id:int):
    pass

@app.post('/items', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    new_item = models.Item(
        desc = item.description,
        price_range = item.price_range
    )

    db.add(new_item)
    db.commit()
    
    return new_item
    
@app.put('/item/{item_id}')
def update_an_item(item_id:int):
    pass

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    pass