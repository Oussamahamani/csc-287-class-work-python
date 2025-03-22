from pathlib import Path
import json
import plotly.express as px

path = Path('eq_data/eq_data_1_day_m1.geojson')

contents = path.read_text(encoding="utf8")
all_eq_data = json.loads(contents)
all_eq_dicts = all_eq_data['features']



mags, lons, lats, eq_titles = [], [], [], []
# — SNIP —
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# — SNIP —
for eq_dict in all_eq_dicts:
    eq_titles.append(eq_dict['properties']['title'])

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
    color=mags,
    color_continuous_scale='Viridis',
    labels={'color':'Magnitude'},
    projection='natural earth',
    hover_name=eq_titles,
)
fig.show()