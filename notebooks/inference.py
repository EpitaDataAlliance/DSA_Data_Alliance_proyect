import pandas as pd
import numpy as np
import os
import joblib


ROOT_DIR = os.path.dirname(os.path.abspath(''))


def making_predictions_using_model(x_predict: pd.DataFrame):
    filename = os.path.join(ROOT_DIR + '/models', 'model.joblib')

    reg_multiple_load = joblib.load(filename)

    y_pred = reg_multiple_load.predict(x_predict)

    return y_pred


def make_predictions(input_data: pd.DataFrame) -> np.ndarray:
    # the model and all the data preparation objects
    # (encoder, etc) should be loaded from the models folder

    data_test = input_data.drop('id',axis=1)

    y_pred = making_predictions_using_model(data_test)

    return y_pred
