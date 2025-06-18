import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Get base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Correct path to cleaned data
file = os.path.join(base_dir, "../data/cleaned_power_data.csv")

# Load the cleaned data
df = pd.read_csv(file, parse_dates=["datetime"])

# Feature engineering: extract time components
df["hour"] = df["datetime"].dt.hour
df["day"] = df["datetime"].dt.day
df["month"] = df["datetime"].dt.month
df["weekday"] = df["datetime"].dt.weekday

# Define features and target
features = ["hour", "day", "month", "weekday"]
target = "Global_active_power"

X = df[features]
y = df[target]

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Model Evaluation:")
print("MAE:", mean_absolute_error(y_test, y_pred))
import numpy as np
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

print("R²:", r2_score(y_test, y_pred))
