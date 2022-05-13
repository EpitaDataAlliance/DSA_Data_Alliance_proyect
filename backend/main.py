import pandas as pd
# from inference import make_predictions
import os
import joblib
from typing import Optional
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
# from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import json
from pydantic import BaseModel



ROOT_DIR = os.path.dirname(os.path.abspath(""))
MODEL_PATH = "../models"

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
    "wifi": "wifi"
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


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from the other side"}


@app.get("/predict")
def get_predictions_from_params(params: Item):
    model = joblib.load(os.path.join(MODEL_PATH, "model.joblib"))
    row = pd.Series(params.dict().values())
    df = pd.DataFrame()
    df = df.append(row, ignore_index=True)
    df.columns = STYLES.keys()
    prediction = model.predict(df)
    prediction = prediction.tolist()

    return {"predictions": prediction}


@app.post("/predictFile")
def get_predictions_from_file(file: UploadFile = File(...)):
    file_content = file.file.read()
    file_content = file_content.decode("utf-8")
    file_content = file_content.split("\n")
    file_content = [x.split(",") for x in file_content]
    file_content = pd.DataFrame(file_content)
    file_content.columns = list(STYLES.values())
    file_content = file_content.astype(float)
    model = joblib.load(os.path.join(MODEL_PATH, "model.joblib"))
    predictions = model.predict(file_content)
    return {"predictions": predictions}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
