# src/train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/traffic_data.csv")

# One-hot encode categorical features
df_encoded = pd.get_dummies(df[['time', 'location', 'day_of_week']], columns=['location', 'day_of_week'])
X = df_encoded
y = df['congestion_level']

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "models/congestion_model.joblib")
print("✅ Model saved as models/congestion_model.joblib")