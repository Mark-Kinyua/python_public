import numpy as np
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, LSTM, Dense

# Lets shake the finance industry just abit by outplaying them with the law of economics..

# Loading data
company = ["TSLA", "FB", "AMZN", "GOOG", "NFLX"]

for comp in company:
    start = dt.datetime(2012, 1, 1)
    end = dt.datetime.now()


    def data_reader(comp, begin, mwisho):
        try:
            ddata = web.DataReader(comp, 'iex', begin, mwisho)
            ddata.index = pd.to_datetime(ddata.index)
        except:
            ddata = web.get_data_yahoo(
                comp, begin, mwisho
            )
        return ddata


    data = data_reader(comp, start, end)

    # Prepare data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

    prediction_days = 400

    x_train = []
    y_train = []

    for x in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[x - prediction_days:x, 0])
        y_train.append(scaled_data[x, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # Build the models

    model = Sequential()

    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))  # Prediction of next closing values

    model.compile(optimizer='adam', loss='mean_squared_error')
    hist = model.fit(x_train, y_train, epochs=50, batch_size=32)
    model.save(f'{comp}_model.model', hist)
