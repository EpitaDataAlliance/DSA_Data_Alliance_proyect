from fastapi import FastAPI
import pandas as pd
from inference import make_predictions
import os
import joblib

ROOT_DIR = os.path.dirname(os.path.abspath(''))

app = FastAPI()


@app.get("/")
async def root():

    filename_test = os.path.join(ROOT_DIR + '/data', 'test.csv')
    user_data_df = pd.read_csv(filename_test)
    predictions = make_predictions(user_data_df)
    predictions


    return predictions
