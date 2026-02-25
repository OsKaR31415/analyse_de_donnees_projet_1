import requests
import pandas as pd
from io import StringIO

url = (
    "https://sdmx.oecd.org/public/rest/data/OECD.CFE.EDS,DSD_REG_ECO@DF_GDP,/A..AUS+AU1+AU2+AU3+AU4+AU5+AU6+AU7+AU8+AUT+AT11+AT111+AT112+AT113+AT12+AT121+AT122+AT123+AT124+AT125+AT126+AT127+AT13+AT130+AT21+AT211+AT212+AT213+AT22+AT221+AT222+AT223+AT224+AT225+AT226+AT31+AT311+AT312+AT313+AT314+AT315+AT32+AT321+AT322+AT323+AT33+AT331+AT332+AT333+AT334+AT335+AT34+AT341+AT342..GDP..Q.USD_PPP_PS?dimensionAtObservation=AllDimensions"
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

import plotly.express as px

# 1) clean types
tmp = df.copy()
tmp["OBS_VALUE"] = pd.to_numeric(tmp["OBS_VALUE"], errors="coerce")
tmp["TIME_PERIOD"] = pd.to_numeric(tmp["TIME_PERIOD"], errors="coerce")

country_col = "Reference area" if "Reference area" in tmp.columns else "REF_AREA"

# 2) one value per (country, year)  [sum is common; use mean if it fits your variable better]
g = (
    tmp.dropna(subset=["TIME_PERIOD", "OBS_VALUE"])
       .groupby([country_col, "TIME_PERIOD"], as_index=False)["OBS_VALUE"]
       .sum()
       .sort_values("TIME_PERIOD")
)

# 3) plot: one colored line per country
fig = px.line(
    g,
    x="TIME_PERIOD",
    y="OBS_VALUE",
    color=country_col,
    markers=True,
    title="GDP per capita (local currency units) over time by country",
    labels={"TIME_PERIOD": "Year", "OBS_VALUE": "GDP per capita"}
)

fig.show()
