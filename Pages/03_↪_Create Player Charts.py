import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import plotly_express as px
import numpy as np

df = pd.read_csv('./Desktop/SiteStats/All_Yearly_Stats.csv')
df2022 = pd.read_csv('./Desktop/SiteStats/Yearly_Stats_2022.csv')

st.title('Create Custom Player Charts')

x_axis_val =  st.selectbox('Select X-Axis', options=df.columns[3:19])
y_axis_val =  st.selectbox('Select Y-Axis', options=df.columns[3:19])

st.write(' ')

year = st.selectbox(
    'Select A Season',
    ('Every Season', '2022')
)

st.write("Double click to reset chart")

if year == "Every Season":
    plots = px.scatter(df, x=x_axis_val, y=y_axis_val, hover_name=df.Player, hover_data=['GP'], title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val))

    if st.checkbox('Plot Names'):
        plots = px.scatter(df, x=x_axis_val, y=y_axis_val, hover_name=df.Player, hover_data=['GP'], title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val), text=df.Player)

    if st.button('Plot Chart'):
        st.plotly_chart(plots)
else:
    plots = px.scatter(df2022, x=x_axis_val, y=y_axis_val, hover_name=df2022.Player, hover_data=['GP'], title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val))

    if st.checkbox('Plot Names'):
        plots = px.scatter(df2022, x=x_axis_val, y=y_axis_val, hover_name=df2022.Player, hover_data=['GP'], title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val), text=df2022.Player)

    if st.button('Plot Chart'):
        st.plotly_chart(plots)