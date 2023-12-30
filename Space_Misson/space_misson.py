import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from iso3166 import countries
from datetime import datetime, timedelta

pd.options.display.float_format = '{:,.2f}'.format
df_data = pd.read_csv('mission_launches.csv')
clean_data = df_data.dropna()

# Created a chart that shows the number of space mission launches by organisation.
organisation = clean_data.Organisation.value_counts()
fig1 = px.bar(organisation, x=organisation.index, y=organisation.values, labels={"y": 'Number of Lunches'})
# fig.write_html("launch_per_organisation.html")

# Use a Choropleth Map to Show the Number of Launches by Country
df_data['Country'] = df_data['Location'].apply(lambda location: location.split(",")[-1].strip())
clean_data['Country'] = clean_data['Location'].apply(lambda location: location.split(",")[-1].strip())
replacements = {
    "Russia" : "Russian Federation",
    'New Mexico': 'USA',
    'Yellow Sea': 'China',
    'Pacific Missile Range Facility': 'USA',
    'Shahrud Missile Test Site': 'Iran, Islamic Republic of',
    'Barents Sea': 'Russian Federation',
    'Gran Canaria': 'USA',
    'Pacific Ocean': 'USA',
    'North Korea': "Korea, Democratic People's Republic of",
    'South Korea': 'Korea, Republic of',
    'Iran': 'Iran, Islamic Republic of'
}

for old_value, new_value in replacements.items():
    df_data.loc[df_data.Country == old_value, 'Country'] = new_value
for old_value, new_value in replacements.items():
    clean_data.loc[clean_data.Country == old_value, 'Country'] = new_value
country = df_data.groupby("Country",as_index=False).size()
country["alpha3"] = country.Country.apply(lambda country: (countries.get(country)).alpha3)
fig2 = px.choropleth(country, locations="alpha3",
                    color="size", # lifeExp is a column of gapminder
                    hover_data= {"size": True, "Country": True,"alpha3":False},
                    labels={ "Country": " Country", "size": " Number of Launches",},
                    color_continuous_scale=px.colors.sequential.matter)
# fig.write_html("launch_per_country.html")
# fig2.show()

# Created a Plotly Sunburst Chart of the countries, organisations, and mission status.
clean_data["ISO"]=clean_data.Country.apply(lambda country: countries.get(country).alpha3)
fig3 = px.sunburst(clean_data, path=['ISO', 'Organisation', 'Mission_Status'])
# fig3.show()
# fig3.write_html("mission_status.html")