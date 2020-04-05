import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import matplotlib.pyplot as plt

# import NYT data
df = pd.read_csv('covid-19-data/us-states.csv')  

# Growth rate by state
NYonly = df[df['state']=='New York']
NYdate = NYonly["date"].to_numpy()
NYcases = NYonly["cases"].to_numpy()
NYdeaths = NYonly["deaths"].to_numpy()
# NYdate_both = NYonly[["date","cases", "deaths"]]


# fig = go.Figure()
# fig.add_trace(go.Scatter(x=NYdate, y=NYcases, mode = 'lines+markers', name='Cases'))
# fig.add_trace(go.Scatter(x=NYdate, y=NYdeaths, mode = 'lines+markers', name='Deaths'))
# fig.update_layout( yaxis_type="log")
# fig.show()



# Counties plotted in
df_county = pd.read_csv('covid-19-data/us-counties.csv', dtype={'fips': object})
current_date_only = df_county[df_county['date'] == '2020-04-03']
# print(current_date_only)
# cali = current_date_only[current_date_only['state'] == 'Georgia']
# print(cali)

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
# print(counties)
fig = px.choropleth_mapbox(current_date_only, geojson=counties,  locations='fips', color='cases',
                            color_continuous_scale="Viridis",
                           range_color=(0,1.5e4),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity = .5,
                          )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

# Plot in dash
# https://plotly.com/python/renderers/#displaying-plotly-figures
# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter