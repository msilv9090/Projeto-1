import pandas as pd 
import stramlit as st

dataset = pd.read_csv('https://www.irdx.com.br/media/uploads/paises.csv')

st.dataframe(dataset)
