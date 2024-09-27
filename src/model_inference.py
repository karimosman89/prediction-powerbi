import joblib
import pandas as pd

def predict_churn(data):
    model = joblib.load('models/churn_model.pkl')
    predictions = model.predict(data)
    return predictions
