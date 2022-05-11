
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_log_error
from preprocess import feature_engineering
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier


ROOT_DIR = os.path.dirname(os.path.abspath(''))



def model_building(d_train: pd.DataFrame):
    
    data_x_train, y_training = feature_engineering(d_train)
    model_training(data_x_train, y_training)



def model_training(
    data_x_train: pd.DataFrame,
    y_training: pd.DataFrame):

    knn =  KNeighborsClassifier(n_neighbors = 10)
    knn.fit(data_x_train, y_training)
    filename = os.path.join(ROOT_DIR + '/models', 'model.joblib')
    joblib.dump(knn, filename)

def model_predictions(
        data_x_train: pd.DataFrame, y_test: pd.DataFrame):

    filename = os.path.join(ROOT_DIR + '/models', 'model.joblib')
    model_load = joblib.load(filename)

    y_pred = model_load.predict(data_x_train)

    return classification_report(y_test,y_pred)


def model_evaluation(d_test: pd.DataFrame):

    data_x_train, y_test = feature_engineering(d_test)

    model_performance = model_predictions(data_x_train, y_test)

    return model_performance



def build_model(data: pd.DataFrame):
    d_train, d_test = train_test_split(data, test_size=0.2)

    model_building(d_train)
    model_performance = model_evaluation(d_test)

    return model_performance