import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
#from streamlit_option_menu import option_menu
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from PIL import Image

st.set_page_config(
    page_title="Automatic Stats",
    page_icon="©",
)

with st.sidebar:
    st.write("This code will be printed to the sidebar.")


st.title("Automatic Stats")

st.write("Unique and Easily Accessible NBA Stats")

from PIL import Image

image = Image.open('Giannis.png')
st.image(image)
