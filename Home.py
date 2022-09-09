import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Automatic Stats",
    page_icon="©",
)

st.title("Automatic Stats")

st.write("Unique and Easily Accessible NBA Stats")

from PIL import Image
image = Image.open('./Files&Images/Giannis.png')
st.image(image)
