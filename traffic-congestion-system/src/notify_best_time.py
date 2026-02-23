# src/notify_best_time.py
import pandas as pd
import joblib
from datetime import datetime, timedelta

# Load dataset and model
df = pd.read_csv("data/traffic_data.csv")
model = joblib.load("models/congestion_model.joblib")

# Example: find best time to leave today
today = datetime.today().strftime("%A")  # e.g., "Monday"
best_time = None
lowest_congestion = 10

for hour in range(6, 22):
    temp_df = df[(df['time']==hour) & (df['day_of_week']==today)]
    if temp_df.empty:
        continue
    df_encoded = pd.get_dummies(temp_df[['time', 'location', 'day_of_week']], columns=['location', 'day_of_week'])
    prediction = model.predict(df_encoded)
    avg_congestion = prediction.mean()
    if avg_congestion < lowest_congestion:
        lowest_congestion = avg_congestion
        best_time = hour

if best_time is not None:
    print(f"🕒 Best time to leave today ({today}): {best_time}:00")
else:
    print(f"No traffic data available for {today}")