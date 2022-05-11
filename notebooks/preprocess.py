# for cleansing and feature engineering functions
import pandas as pd
import os


def feature_engineering(d_train: pd.DataFrame):


    data_x = d_train.drop(['price_range'], axis=1)

    y_training = d_train['price_range'].values.reshape(-1,1)

    return data_x, y_training
