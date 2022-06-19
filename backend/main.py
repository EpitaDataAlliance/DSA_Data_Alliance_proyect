from datetime import datetime
import pandas as pd
import os
import joblib
import uvicorn
import json

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine


ROOT_DIR = os.path.dirname(os.path.abspath(""))
MODEL_PATH = "./models"
HOST = '0.0.0.0'
PORT = 5000


models.Base.metadata.create_all(bind=engine)

# wake DB up
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


class JsonDfItem(BaseModel):
    dataframe1: str
    class Config:
        arbitrary_types_allowed = True


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from the other side"}


@app.get("/predict")
def get_predictions_from_params(params: Item, db: Session = Depends(get_db)):
    model = joblib.load(os.path.join(MODEL_PATH, "model.joblib"))
    row = pd.Series(params.dict().values())
    df = pd.DataFrame()
    df = df.append(row, ignore_index=True)
    df.columns = STYLES.keys()
    predictions = model.predict(df)
    predictions = predictions.tolist()

    db_dict = {
        "prediction": predictions[0],
        "datetime": datetime.now(),
        "params": json.dumps(params.dict()),
    }
    # save to db
    crud.create_prediction(db, prediction=db_dict)

    return {"predictions": predictions}


@app.post("/predictjson")
def get_predictions_from_json(payload: JsonDfItem):
    model = joblib.load(os.path.join(MODEL_PATH, "model.joblib"))
    df = pd.read_json(payload.dataframe1)
    df = df.drop(columns=["id"])
    predictions = model.predict(df)
    predictions = predictions.tolist()
    # here params need to be exported from csv and then should be saved asa in get_predictions_from_params

    return {"predictions": predictions}



@app.get('/predictions/', response_model=List[schemas.Prediction])
def read_predictions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    predictions = crud.get_predictions(db, skip=skip, limit=limit)

    return predictions



if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=PORT, log_level="info")
