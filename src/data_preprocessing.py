import pandas as pd

def preprocess_customer_data(data):
    data['Tenure'] = data['End Date'] - data['Start Date']
    data['Tenure'] = data['Tenure'].dt.days
    data = pd.get_dummies(data, drop_first=True)  # One-hot encoding for categorical variables
    return data
