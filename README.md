
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

## 🚀 Deployment

This app is live on **Streamlit Community Cloud**:  
🌐 [business-conditions-index.streamlit.app](https://business-conditions-index.streamlit.app/)

### ✅ Option 1: Deploy Your Own (Streamlit Cloud)

1. Fork or clone this repo to your own GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and click **“New App”**
3. Configure the deployment:
   - **Repository:** `your-username/business-conditions-index`
   - **Branch:** `main`
   - **Main file:** `bci.py`
4. Streamlit automatically uses the `environment.yml` file to install dependencies.

---

### 💻 Option 2: Run Locally

Clone the repo and run locally using either Conda or pip.

**Using Conda**:

```bash
conda env create -f environment.yml
conda activate bci_env
```

**Using pip** (fallback):

```bash
pip install -r requirements.txt
```

### 🗂️ Prepare Your Data

Ensure these files are in your working directory (or generate them using `stationarize_fred_qd.py`):

- `fred_qd_cached.csv`
- `fred_qd_transformation.csv`

### 🚀 Launch the App

```bash
streamlit run bci.py
```

### 🧬 Clone the Repository

If you haven't already:

```bash
git clone https://github.com/csharpconsultant/business-conditions-index.git
cd business-conditions-index
```

---

## 📦 Dependencies

Managed via `environment.yml`. Key packages include:

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

Created by Anthony Vuolo  
Let’s connect on [LinkedIn](https://www.linkedin.com)
