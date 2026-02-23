# src/generate_dataset.py
import pandas as pd
import random
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Sample data generation
locations = ['L1', 'L2', 'L3', 'L4', 'L5']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

data = []
for hour in range(6, 22):  # 6 AM to 9 PM
    for loc in locations:
        for day in days:
            congestion = random.randint(0, 3)  # 0=Low, 3=High
            data.append([hour, loc, day, congestion])

df = pd.DataFrame(data, columns=['time', 'location', 'day_of_week', 'congestion_level'])

# Save dataset
df.to_csv("data/traffic_data.csv", index=False)
print("✅ Dataset saved as data/traffic_data.csv")