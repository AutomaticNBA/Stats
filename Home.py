import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("Automatic Stats")

st.write("Unique and Easily Accessible NBA Stats")

from PIL import Image
image = Image.open('././Desktop/SiteStats/Giannis.png')
st.image(image)