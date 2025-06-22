import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from stationarize_fred_qd import load_and_transform
import altair as alt

# App config
st.set_page_config(page_title="Business Conditions Index", layout="wide")
st.title("📈 Business Conditions Index from FRED-QD")

@st.cache_data
def load_data():
    return load_and_transform("fred_qd_cached.csv", "fred_qd_transformation.csv")

# Load and prepare data
df = load_data()
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)
df.index = pd.to_datetime(df.index)

# PCA
X = StandardScaler().fit_transform(df)
pca = PCA(n_components=1)
z = pca.fit_transform(X).flatten()

# Flip sign if negatively correlated with GDP
if 'GDPC1' in df.columns and np.corrcoef(z, df['GDPC1'].values[:len(z)])[0, 1] < 0:
    z *= -1

bci = pd.Series(z, index=df.index[:len(z)], name="Business Conditions Index")
bci_df = bci.reset_index()
bci_df.columns = ['Date', 'BCI']

# Get latest BCI value and formatted date
latest_date = bci_df["Date"].max()
latest_value = bci_df.loc[bci_df["Date"] == latest_date, "BCI"].values[0]
latest_label = latest_date.strftime("%B %Y")

# Explanatory text
st.markdown(f"""
### ℹ️ How to Interpret the Business Conditions Index (BCI)

The **Business Conditions Index (BCI)** summarizes broad economic conditions using the first principal component (PC1) of many macroeconomic indicators from the FRED-QD dataset. It is a standardized measure, meaning:

- **BCI > 0** indicates economic activity is **above average** relative to historical norms.
- **BCI < 0** indicates economic activity is **below average**.
- The BCI is centered around **zero**, with larger absolute values indicating stronger deviations from typical economic conditions.

As of **{latest_label}**, the BCI is **{latest_value:.2f}**, suggesting that U.S. business conditions are **{"slightly below" if latest_value < 0 else "slightly above"} average**.

This index is similar in spirit to the Weekly Economic Index (WEI), but computed from quarterly FRED-QD data using Principal Component Analysis (PCA).
""")

# Data preview
st.subheader("✅ Transformed & Cleaned Stationary Data")
st.write("Data shape after final cleaning:", df.shape)

with st.expander("📄 View Data Table"):
    st.dataframe(df.head())

# Date range selector
st.subheader("🗓️ Select Date Range for BCI View")
min_date = bci_df["Date"].min().date()
max_date = bci_df["Date"].max().date()

date_range = st.slider(
    "Choose date range:",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="YYYY-MM"
)

filtered_bci_df = bci_df[
    (bci_df["Date"] >= pd.to_datetime(date_range[0])) &
    (bci_df["Date"] <= pd.to_datetime(date_range[1]))
]

# Zero line as horizontal rule
zero_line = alt.Chart(pd.DataFrame({'y': [0]})).mark_rule(
    color='black', strokeWidth=2
).encode(y='y:Q')

# Main BCI chart
main_line = alt.Chart(filtered_bci_df).mark_line(color='steelblue').encode(
    x=alt.X('Date:T', axis=alt.Axis(title='Date', format='%Y', grid=True)),
    y=alt.Y('BCI:Q', axis=alt.Axis(
        title='Business Conditions Index',
        grid=True,
        tickCount=10,
        domain=True
    )),
    tooltip=['Date:T', 'BCI:Q']
).properties(
    width=800,
    height=400
)

combined_chart = (main_line + zero_line).configure_axis(
    gridColor='lightgray',
    gridOpacity=0.7,
    domain=True
).configure_view(
    stroke=None
)

st.altair_chart(combined_chart)

st.write("Explained Variance by PC1:", round(pca.explained_variance_ratio_[0] * 100, 2), "%")

# Zoomed-in BCI chart (last 4 years)
st.subheader("🔍 Business Conditions Index – Since 1-1-2023")
recent_bci_df = bci_df[bci_df["Date"] >= pd.to_datetime("2023-01-01")]

zoom_line = alt.Chart(recent_bci_df).mark_line(color='steelblue').encode(
    x=alt.X('Date:T', axis=alt.Axis(title='Quarter', format='%Y-%m', grid=True)),
    y=alt.Y('BCI:Q', axis=alt.Axis(title='BCI', grid=True)),
    tooltip=['Date:T', 'BCI:Q']
).properties(width=800, height=300)

zoom_combined = (zoom_line + zero_line).configure_axis(
    gridColor='lightgray',
    gridOpacity=0.7,
    domain=True
).configure_view(
    stroke=None
)

st.altair_chart(zoom_combined)

# PCA variable descriptions
st.subheader("📘 Variables Used in the Business Conditions Index")

pca_descriptions = {
    "GDPC1": "Real Gross Domestic Product (Chained 2012 Dollars)",
    "PCECC96": "Real Personal Consumption Expenditures",
    "PCDGx": "Real PCE: Durable Goods",
    "PCNDx": "Real PCE: Nondurable Goods",
    "PCESVx": "Real PCE: Services",
    "INDPRO": "Industrial Production Index",
    "PAYEMS": "Total Nonfarm Payrolls",
    "HOUST": "Housing Starts: Total New Privately Owned",
    "PERMIT": "New Private Housing Permits",
    "RETAILx": "Real Retail and Food Services Sales (excluding autos)",
    "UNRATE": "Civilian Unemployment Rate",
    "CPIAUCSL": "Consumer Price Index for All Urban Consumers (All Items)",
    "FEDFUNDS": "Effective Federal Funds Rate",
    "GS10": "10-Year Treasury Constant Maturity Rate",
    "M2SL": "M2 Money Stock (NSA)",
    "BUSLOANS": "Commercial and Industrial Loans",
    "RECPROUSM156N": "NBER Recession Probabilities (Smoothed)",
    "CLAIMSx": "Initial Unemployment Claims",
    "CE16OV": "Civilian Employment Level (Age 16+)",
    "AWHMAN": "Average Weekly Hours: Manufacturing"
}

desc_df = pd.DataFrame(list(pca_descriptions.items()), columns=["Variable", "Description"])

with st.expander("📄 View PCA Variable Descriptions"):
    st.dataframe(desc_df)



# Download button
st.download_button(
    label="📥 Download BCI as CSV",
    data=bci.to_csv().encode(),
    file_name="business_conditions_index.csv",
    mime="text/csv"
)
