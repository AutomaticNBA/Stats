import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from PIL import Image

st.title("Regular Season Shooting Stats")

st.subheader("Paint Scoring Seasons Since 1997")
df1 = pd.read_csv('./Desktop/SiteStats/All_Paint_Scoring_Seasons.csv')
AgGrid(df1, height=314)

image = Image.open('./Desktop/SiteStats/Shaq.png')
st.image(image)

st.write(' ')

df2 = pd.read_csv('./Desktop/SiteStats/All_Outside_Scoring_Seasons.csv')
st.subheader("Outside Scoring Seasons Since 1997")
AgGrid(df2, height=314)

image = Image.open('./Desktop/SiteStats/Curry.png')
st.image(image)

st.write(' ')

df3 = pd.read_csv('./Desktop/SiteStats/All_Mid_Range_Seasons.csv')
st.subheader("Midrange Scoring Seasons Since 1997")
AgGrid(df3, height=314)

image = Image.open('./Desktop/SiteStats/Durant.png')
st.image(image)
