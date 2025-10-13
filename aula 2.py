import pandas as pd 
import stramlit as st

dataset = pd.read_csv('https://www.irdx.com.br/media/uploads/paises.csv')

import plotly.express as px
fig = px.scatter_geo(dataset,
                     lat=dataset['latitude'],
                     lon=dataset['longitude'],
                     hover_name=dataset['nome'])

fig.update_layout(title='Mapa Coroplético dos Países', geo_scope='world')

st.plotly_chart(fig, use_container_width=True, theme="streamlit)
