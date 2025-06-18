import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define path dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(BASE_DIR, '../data/individual+household+electric+power+consumption/household_power_consumption.txt')

# Load dataset
df = pd.read_csv(
    file,
    sep=';',
    na_values='?',
    low_memory=False
)

# Combine Date and Time into datetime
df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], dayfirst=True)
df.drop(columns=['Date', 'Time'], inplace=True)

# Convert numeric columns
for col in df.columns:
    if col != 'datetime':
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Now you can continue with plotting/EDA


# Plot 1: Line plot of Global Active Power over time
plt.figure(figsize=(10, 5))
plt.plot(df['datetime'], df['Global_active_power'], color='blue')
plt.title('Global Active Power Over Time')
plt.xlabel('Time')
plt.ylabel('Global Active Power (kilowatts)')
plt.tight_layout()
plt.show()

# Plot 2: Histogram of Voltage
plt.figure(figsize=(8, 4))
sns.histplot(df['Voltage'], bins=50, kde=True)
plt.title('Voltage Distribution')
plt.xlabel('Voltage')
plt.tight_layout()
plt.show()

# Plot 3: Boxplot for Sub-metering
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']])
plt.title('Sub Metering Distribution')
plt.tight_layout()
plt.show()

# ========== Plot 1: Missing Values Heatmap ==========
plt.figure(figsize=(10, 4))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.tight_layout()
plt.show()

# ========== Plot 2: Correlation Matrix ==========
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Correlation Between Features")
plt.tight_layout()
plt.show()

# ========== Plot 3: Global Active Power Over Time ==========
plt.figure(figsize=(15, 4))
plt.plot(df['datetime'], df['Global_active_power'], color='blue', linewidth=0.5)
plt.title("Global Active Power Over Time")
plt.xlabel("Date")
plt.ylabel("Global Active Power (kilowatts)")
plt.tight_layout()
plt.show()

# ========== Plot 4: Sub-Metering Over Time ==========
plt.figure(figsize=(15, 4))
plt.plot(df['datetime'], df['Sub_metering_1'], label='Sub_metering_1')
plt.plot(df['datetime'], df['Sub_metering_2'], label='Sub_metering_2')
plt.plot(df['datetime'], df['Sub_metering_3'], label='Sub_metering_3')
plt.title("Energy Sub-Metering Over Time")
plt.xlabel("Date")
plt.ylabel("Energy (watt-hour)")
plt.legend()
plt.tight_layout()
plt.show()

# Resample to daily mean
daily_avg = df.set_index('datetime').resample('D').mean()

plt.figure(figsize=(15, 4))
plt.plot(daily_avg.index, daily_avg['Global_active_power'], color='green')
plt.title("Daily Average Global Active Power")
plt.xlabel("Date")
plt.ylabel("Kilowatts")
plt.tight_layout()
plt.show()

df['hour'] = df['datetime'].dt.hour
hourly_avg = df.groupby('hour')['Global_active_power'].mean()

plt.figure(figsize=(8, 4))
sns.lineplot(x=hourly_avg.index, y=hourly_avg.values, marker='o')
plt.title("Average Power Usage by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Avg Global Active Power (kW)")
plt.tight_layout()
plt.show()

plt.savefig('../outputs/daily_avg_power.png', dpi=300)
