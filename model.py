import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("dailyActivity_merged.csv")

# Features
X = df[
    ["TotalSteps", "Calories", "VeryActiveMinutes", "SedentaryMinutes"]
]

# Health score formula
df["HealthScore"] = (
    (df["TotalSteps"] / 15000) * 40 +
    (df["VeryActiveMinutes"] / 60) * 30 +
    (1 - df["SedentaryMinutes"] / 1440) * 30
)

y = df["HealthScore"].clip(0, 100)

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained and saved")
