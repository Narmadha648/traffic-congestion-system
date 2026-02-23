import joblib
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR,"models","congestion_model.pkl")

model = joblib.load(model_path)

def predict_congestion(data):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return int(prediction)