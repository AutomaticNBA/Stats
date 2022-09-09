import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from PIL import Image

st.set_page_config(
    page_title="Automatic Stats",
    page_icon="©",
)

with st.sidebar:
    selected = option_menu(
        menu_title="Browse",
        options=["Home", "Stats"],
    )


if selected == "Home":
    st.title("Automatic Stats")

    st.write("Unique and Easily Accessible NBA Stats")

    from PIL import Image

    image = Image.open('Giannis.png')
    st.image(image)

if selected == "Stats":
    st.title("Regular Season Shooting Stats")

    st.subheader("Paint Scoring Seasons Since 1997")
    df1 = pd.read_csv('./Files&Images/All_Paint_Scoring_Seasons.csv')
    AgGrid(df1, height=314)

    image = Image.open('./Files&Images/Shaq.png')
    st.image(image)

    st.write(' ')

    df2 = pd.read_csv('./Files&Images/All_Outside_Scoring_Seasons.csv')
    st.subheader("Outside Scoring Seasons Since 1997")
    AgGrid(df2, height=314)

    image = Image.open('./Files&Images/Curry.png')
    st.image(image)

    st.write(' ')

    df3 = pd.read_csv('./Files&Images/All_Mid_Range_Seasons.csv')
    st.subheader("Midrange Scoring Seasons Since 1997")
    AgGrid(df3, height=314)

    image = Image.open('./Files&Images/Durant.png')
    st.image(image)