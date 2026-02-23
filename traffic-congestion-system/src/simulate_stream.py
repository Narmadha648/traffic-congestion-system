# src/simulate_stream.py
import pandas as pd
import joblib
import time
from email_alert import send_email
import os

# Load dataset
df = pd.read_csv("data/traffic_data.csv")

# One-hot encode categorical features (same as training)
df_encoded = pd.get_dummies(df[['time', 'location', 'day_of_week']], columns=['location', 'day_of_week'])

# Load trained model
model_path = "models/congestion_model.joblib"
model = joblib.load(model_path)

print("🚦 Starting Traffic Simulation...")

for i in range(0, len(df)):
    row = df.iloc[i]
    row_encoded = df_encoded.iloc[i:i+1]
    prediction = model.predict(row_encoded)[0]
    print(f"Location: {row['location']}")
    print(f"Predicted Congestion Level: {prediction}")
    print("----------------------------------------")

    # Send email if congestion is high
    if prediction >= 2:
        subject = f"Traffic Alert for {row['location']}"
        body = f"Congestion Level: {prediction} at {row['time']}:00 on {row['day_of_week']}. Consider leaving earlier!"
        send_email(subject, body, "recipient_email@example.com")  # Replace with your recipient

    time.sleep(1)  # simulate delay