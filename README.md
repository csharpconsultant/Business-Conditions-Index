
# 📈 Business Conditions Index (BCI) using FRED-QD Data

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://business-conditions-index.streamlit.app/)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Last Commit](https://img.shields.io/github/last-commit/csharpconsultant/business-conditions-index)


This project computes a **Business Conditions Index (BCI)** for the U.S. economy using **Principal Component Analysis (PCA)** on macroeconomic indicators from the **FRED-QD** dataset. Inspired by academic and Federal Reserve research, this index provides a transparent, reproducible tool for summarizing the U.S. business cycle from a large number of indicators.

---

## 🔍 Overview

- **Goal:** Summarize broad U.S. economic conditions into a single index  
- **Method:** First principal component of selected FRED-QD indicators  
- **Framework:** Built with `Streamlit`, `scikit-learn`, `Altair`, and `pandas`

---

## 📊 Key Features

- Uses 20+ macroeconomic time series from FRED-QD (GDP, CPI, Retail Sales, etc.)
- Automatically standardizes and stationarizes data
- Performs PCA and dynamically flips sign for economic interpretability
- Visualizes the index over time, including zoomed views and tooltips
- Includes variable descriptions and CSV download for further analysis

---

## 🚀 Getting Started

### 1. 🚀 Deployment

This app runs on [Streamlit Community Cloud](https://streamlit.io/cloud).

### ✅ Option 1: Deploy via Streamlit (recommended)

1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and click **“New App”**
3. Select:
   - Repository: `csharpconsultant/business-conditions-index`
   - Branch: `main`
   - File: `bci.py`
4. Streamlit will automatically detect the `environment.yml` and install dependencies.

### 💻 Option 2: Run locally

If you'd like to run the app on your machine:

```bash
git clone https://github.com/csharpconsultant/business-conditions-index.git
cd business-conditions-index
conda env create -f environment.yml
conda activate bci_env
streamlit run bci.py

### 2. Prepare your data

Ensure these files are in your working directory (or generate them using `stationarize_fred_qd.py`):

- `fred_qd_cached.csv`
- `fred_qd_transformation.csv`

### 3. Launch the app

```bash
streamlit run bci.py
```

---

## 📁 File Structure

```
.
├── bci.py                  # Main Streamlit app
├── stationarize_fred_qd.py     # Data transformation utility
├── fred_qd_cached.csv          # Transformed macroeconomic data
├── fred_qd_transformation.csv  # Variable transformation mapping
├── environment.yml                   # environment specification
├── README.md                   # This file
```

---

## 🧾 Variables Used in the BCI

| Variable     | Description                                           |
|--------------|-------------------------------------------------------|
| `GDPC1`      | Real Gross Domestic Product (Chained 2012 Dollars)    |
| `PCECC96`    | Real Personal Consumption Expenditures                |
| `PCDGx`      | Real PCE: Durable Goods                               |
| `PCNDx`      | Real PCE: Nondurable Goods                            |
| `PCESVx`     | Real PCE: Services                                    |
| `INDPRO`     | Industrial Production Index                           |
| `PAYEMS`     | Total Nonfarm Payrolls                                |
| `HOUST`      | Housing Starts: Total New Privately Owned             |
| `PERMIT`     | New Private Housing Permits                           |
| `RETAILx`    | Real Retail and Food Services Sales (excl. autos)     |
| `UNRATE`     | Civilian Unemployment Rate                            |
| `CPIAUCSL`   | Consumer Price Index (All Urban Consumers)            |
| `FEDFUNDS`   | Effective Federal Funds Rate                          |
| `GS10`       | 10-Year Treasury Constant Maturity Rate               |
| `M2SL`       | M2 Money Stock (NSA)                                  |
| `BUSLOANS`   | Commercial and Industrial Loans                       |
| `RECPROUSM156N` | NBER Recession Probabilities (Smoothed)            |
| `CLAIMSx`    | Initial Unemployment Claims                           |
| `CE16OV`     | Civilian Employment Level (Age 16+)                   |
| `AWHMAN`     | Average Weekly Hours: Manufacturing                   |

---

## 📦 Dependencies

Managed via `conda.txt`. Key packages include:

- `streamlit`
- `altair`
- `pandas`
- `scikit-learn`
- `numpy`

---

## 📜 License

MIT License — use, modify, and share freely.

---

## 🙌 Acknowledgments

This project was inspired by research and techniques covered in the **Machine Learning II** course for the **Master’s in Economics** program at **Purdue University**.

Special thanks to:

- **Professor Joshua Chan** — [joshuachan.org](https://joshuachan.org/)  
  His lectures introduced PCA-based business cycle tracking as a tool for structural macroeconomic analysis.

- **Federal Reserve Economic Datasets**:
  - [FRED-QD](https://research.stlouisfed.org/econ/mccracken/fred-databases/)
  - [ADS Index (Philadelphia Fed)](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/ads)
  - [Chicago Fed National Activity Index (CFNAI)](https://www.chicagofed.org/research/data/cfnai/current-data)

---

## 🔗 Connect

Created by Tony Vuolo 
Let’s connect on [LinkedIn](https://www.linkedin.com/in/tonyvuolo/)
