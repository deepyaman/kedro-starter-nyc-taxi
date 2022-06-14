from typing import Tuple

import mlflow
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def train(train_data: pd.DataFrame) -> Tuple[pd.DataFrame, LinearRegression]:
    mlflow.sklearn.autolog()

    print(train_data.columns)

    # Split the data into input(X) and output(y)
    y = train_data["cost"]
    # X = train_data.drop(['cost'], axis=1)
    X = train_data[
        [
            "distance",
            "dropoff_latitude",
            "dropoff_longitude",
            "passengers",
            "pickup_latitude",
            "pickup_longitude",
            "store_forward",
            "vendor",
            "pickup_weekday",
            "pickup_month",
            "pickup_monthday",
            "pickup_hour",
            "pickup_minute",
            "pickup_second",
            "dropoff_weekday",
            "dropoff_month",
            "dropoff_monthday",
            "dropoff_hour",
            "dropoff_minute",
            "dropoff_second",
        ]
    ]

    # Split the data into train and test sets
    trainX, testX, trainy, testy = train_test_split(X, y, test_size=0.3, random_state=42)
    print(trainX.shape)
    print(trainX.columns)

    # Train a Linear Regression Model with the train set
    model = LinearRegression().fit(trainX, trainy)
    print(model.score(trainX, trainy))

    # test_data = pd.DataFrame(testX, columns = )
    testX["cost"] = testy
    print(testX.shape)
    return testX, model
