import requests
import pandas as pd
from io import StringIO
import plotly.express as px

url = (
    "https://sdmx.oecd.org/public/rest/data/OECD.ELS.SAE,DSD_EARNINGS@GENDER_WAGE_GAP,/......_T?dimensionAtObservation=AllDimensions"
)

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/csv, */*;q=0.1",
}

r = requests.get(url, headers=headers, timeout=60)
print("status:", r.status_code)
r.raise_for_status()

df = pd.read_csv(StringIO(r.text))

print(df.shape)
print(df.columns.tolist())
print(df.head())

# ------------------------------------------------------

# 1)
tmp = df.copy()
tmp["OBS_VALUE"] = pd.to_numeric(tmp["OBS_VALUE"], errors="coerce")
tmp["TIME_PERIOD"] = pd.to_numeric(tmp["TIME_PERIOD"], errors="coerce")

country_col = "Reference area" if "Reference area" in tmp.columns else "REF_AREA"

# 2) one value per (country, year)
g = (
    tmp.dropna(subset=["TIME_PERIOD", "OBS_VALUE"])
       .groupby([country_col, "TIME_PERIOD"], as_index=False)["OBS_VALUE"]
       .mean()
       .sort_values("TIME_PERIOD")
)

# 3) plot
fig = px.line(
    g,
    x="TIME_PERIOD",
    y="OBS_VALUE",
    color=country_col,
    markers=True,
    title="Gender Wage Gap (Median Earnings Difference) Over Time",
    labels={"TIME_PERIOD": "Year", "OBS_VALUE": "Gender Wage Gap (%)"}
)

fig.show()