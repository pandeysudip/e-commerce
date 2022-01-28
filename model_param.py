import joblib
import numpy as np

# defining a function for combining two columns
def avgDuration(c, d):
    if d == 0:
        result = 0
    else:
        result = float(d)/float(c)
    return result

# defing model to predict based on our saved model
def model_load(variables):
    Administrative_Avg=avgDuration(variables[0], variables[61])
    Informational_Avg=avgDuration(variables[2], variables[3])
    ProductRelated_Avg=avgDuration(variables[4], variables[5])
    BounceRates=variables[6]
    ExitRates=variables[7]
    PageValues=variables[8]
    final_variables=[Administrative_Avg,Informational_Avg,
               ProductRelated_Avg,BounceRates,ExitRates,PageValues ]
    # using standardscaler for transformation
    scaler = joblib.load('scaler.pkl')
    X_scaler = scaler.transform([final_variables])

    test_data = scaler.transform(X_scaler)
    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(test_data)

    return prediction
