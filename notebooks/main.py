import pandas as pd
from inference import make_predictions
import os
import joblib
from typing import Optional
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse


ROOT_DIR = os.path.dirname(os.path.abspath(''))

app = FastAPI()

class User(BaseModel):
    user_name: dict

@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):

    print(type(files))


    print("------",files[0])

    print("---",str(files))
    
    #user_data_df = pd.read_csv(files)

    #print(len(user_data_df))






    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@app.get("/hello")
async def root():
    return {"message": "Hello World"}



@app.get("/sa")
async def root():

    filename_test = os.path.join(ROOT_DIR + '/data', 'test.csv')
    user_data_df = pd.read_csv(filename_test)
    predictions = make_predictions(user_data_df)
    predictions


    return predictions
