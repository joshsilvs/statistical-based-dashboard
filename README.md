# Statistical Based Dashboard

This dashboard visualizes intraday market session data to help traders interpret the statistical likelihood of HOD (High of Day) and LOD (Low of Day) formations based on session conditions like Asia, London, and NY1.

## Features
- Filter by day of week and session conditions
- View HOD/LOD percentage distributions
- Percentile tables for MAE/MFE insights
- Interactive scatter plots

## How to Run

1. Clone this repo:
```
git clone https://github.com/YOUR_USERNAME/statistical-based-dashboard.git
cd statistical-based-dashboard
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the app:
```
streamlit run app.py
```

## Data Source
The data comes from manually logged session data and analysis exported from Power BI.
