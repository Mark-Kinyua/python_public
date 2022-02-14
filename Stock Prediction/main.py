import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model


# Loading data
company = ["TSLA", "FB", "AMZN", "GOOG", "NFLX"]

for comp in company:
    start = dt.datetime(2012, 1, 1)
    end = dt.datetime.now()
    prediction_days = 300


    def data_reader(comp, begin, mwisho):
        try:
            ddata = web.DataReader(comp, 'iex', begin, mwisho)
            ddata.index = pd.to_datetime(ddata.index)
        except:
            ddata = web.get_data_yahoo(
                comp, begin, mwisho
            )
        return ddata


    # Load Test Data

    data = data_reader(comp, start, end)

    model = load_model(f'{comp}_model.model')
    test_start = dt.datetime(2020, 1, 1)
    test_end = dt.datetime.now()

    test_data = data_reader(comp, test_start, test_end)
    actual_prices = test_data['Close'].values

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

    total_dataset = pd.concat((data['Close'], test_data['Close']), axis=0)
    model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
    model_inputs = model_inputs.reshape(-1, 1)
    model_inputs = scaler.transform(model_inputs)

    # Make predictions on Test Data

    x_test = []

    for x in range(prediction_days, len(model_inputs)):
        x_test.append(model_inputs[x - prediction_days:x, 0])

    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    predicted_prices = model.predict(x_test)
    predicted_prices = scaler.inverse_transform(predicted_prices)

    # Plot the test predictions
    plt.plot(actual_prices, color="black", label=f"Actual {comp} Prices")
    plt.plot(predicted_prices, color="blue", label=f"Predicted {comp} Prices")
    plt.title(f"{comp} stock Prices")
    plt.xlabel("Time")
    plt.ylabel(f"{comp} share prices")
    plt.legend()
    plt.show()

    # Predicting next day

    real_data = [model_inputs[len(model_inputs) + 1 - prediction_days:len(model_inputs + 1), 0]]
    real_data = np.array((real_data))
    real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))

    prediction = model.predict(real_data)
    prediction = scaler.inverse_transform(prediction)

    print(f"Prediction for {comp} stock price tommorrow is: {prediction}")
