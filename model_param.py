import joblib
import numpy as np

# defining a function for combining two columns


def avgDuration(count, duration):
    count = float(count)
    duration = float(duration)
    if duration == 0 or count == 0:
        result = 0
    elif (count != 0) or (duration != 0):
        result = float(duration)/float(count)
    return result

# defing model to predict based on our saved model


def model_load(variables):
    if variables[0] == '' or variables[1] == '' or variables[2] == '' or variables[3] == '' or variables[4] == '' or variables[5] == '' or variables[6] == '' or variables[7] == '' or variables[8] == '':
        return "Please enter the above information first and click submit. "
    else:
        Administrative_Avg = avgDuration(variables[0], variables[1])
        Informational_Avg = avgDuration(variables[2], variables[3])
        ProductRelated_Avg = avgDuration(variables[4], variables[5])
        BounceRates = variables[6]
        ExitRates = variables[7]
        PageValues = variables[8]
        final_variables = [Administrative_Avg, Informational_Avg,
                           ProductRelated_Avg, BounceRates, ExitRates, PageValues]
        # using standardscaler for transformation
        scaler = joblib.load('scaler.pkl')
        X_scaler = scaler.transform([final_variables])

        test_data = scaler.transform(X_scaler)
        trained_model = joblib.load('model.pkl')
        prediction = trained_model.predict(test_data)
        if prediction == [0]:
            return "Based on your input- 'Customer will not BUY'"
        else:
            return "Based on your input- 'Customer will BUY'"
