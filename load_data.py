import pandas as pd
import os

# Get the base directory (scripts folder)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Correct path to the file with '+' signs
file = os.path.join(base_dir, "../data/individual+household+electric+power+consumption/household_power_consumption.txt")

# 🔍 Print the full path to confirm
print("Looking for file at:", os.path.abspath(file))

# Load dataset
df = pd.read_csv(
    file,
    sep=';',
    parse_dates=[[0, 1]],
    dayfirst=True,
    na_values=['?'],
    low_memory=False
)

# Rename the combined column to 'datetime'
df.rename(columns={'Date_Time': 'datetime'}, inplace=True)

# Move 'datetime' column to front
cols = ['datetime'] + [col for col in df.columns if col != 'datetime']
df = df[cols]

# Convert all columns (except datetime) to numeric
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Clean missing values using forward fill
df.fillna(method='ffill', inplace=True)

# Save cleaned data
cleaned_path = os.path.join(base_dir, "../data/cleaned_power_data.csv")
df.to_csv(cleaned_path, index=False)

# Basic info
print(df.info())
print(df.head())
print('Missing values per column:\n', df.isna().sum())
