import joblib
import numpy as np

# defing model to predict based on our saved model
def model_load(variables):
    # using standardscaler for transformation
    scaler = joblib.load('scaler.pkl')
    X_scaler = scaler.transform([variables])

    test_data = scaler.transform(X_scaler)
    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(test_data)

    return prediction
