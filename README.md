
# ⚡ PowerPulse: Household Energy Usage Forecast

PowerPulse is a data science project aimed at analyzing and forecasting household electricity consumption using historical time-series data. The project applies regression models to deliver insights that help understand and predict future energy usage trends.

---

## 📁 Project Structure

```
PowerPulse/
├── data/
│   └── individual+household+electric+power+consumption/
│       └── household_power_consumption.txt
├── scripts/
│   ├── load_data.py         # Data loading and preprocessing
│   ├── eda.py               # Exploratory Data Analysis
│   └── model.py             # Regression modeling and evaluation
├── requirements.txt         # Required Python packages
└── README.md                # Project overview
```

---

## Dataset

Due to file size restrictions on GitHub, the dataset is hosted externally.

📁 **Download household_power_consumption.txt**:  
[Click here to download](https://drive.google.com/uc?export=download&id=1eGGCsCIs1Kiy-4YRAlwpmvgNrfElOl-j)

After downloading, place the file in the following directory within the project:

s

---

## ⚙️ Setup Instructions

1. **Clone or Download** the repository.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the pipeline scripts in order**:
   - `scripts/load_data.py` – Load and clean the raw dataset
   - `scripts/eda.py` – Visualize and explore consumption patterns
   - `scripts/model.py` – Train and evaluate a regression model

---

## ✅ Model Evaluation

- **Mean Absolute Error (MAE):** ~0.76
- **Root Mean Squared Error (RMSE):** ~1.01
- **R-squared (R²):** ~0.08

> These metrics suggest the model captures general trends but may benefit from further tuning or feature engineering.

---

## 📌 Tools & Technologies

- Python 3
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

---

## 💡 Project Highlights

- Real-world dataset with temporal structure
- Focus on data cleaning, handling missing values, and EDA
- Simple yet effective forecasting using regression techniques

---

## 📬 Contact

For questions, suggestions, or contributions, feel free to reach out. Happy forecasting!
