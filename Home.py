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
        options=["Home","Regular Season Shooting Stats", 'Create Player Charts','Stats Explained']
    )


if selected == "Home":
    st.title("Automatic Stats")

    st.write("Unique and Easily Accessible NBA Stats")

    from PIL import Image

    image = Image.open('Giannis.png')
    st.image(image)

if selected == "Regular Season Shooting Stats":
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

if selected == "Create Player Charts":

    cdf = pd.read_csv('./Files&Images/All_Yearly_Stats.csv')
    df2022 = pd.read_csv('./Files&Images/Yearly_Stats_2022.csv')

    st.title('Create Custom Player Charts')

    x_axis_val = st.selectbox('Select X-Axis', options=cdf.columns[3:19])
    y_axis_val = st.selectbox('Select Y-Axis', options=cdf.columns[3:19])

    st.write(' ')

    year = st.selectbox(
        'Select A Season',
        ('Every Season', '2022')
    )

    st.write("Double click to reset chart")

    if year == "Every Season":
        plots = px.scatter(cdf, x=x_axis_val, y=y_axis_val, hover_name=cdf.Player, hover_data=['GP'],
                           title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val))

        if st.checkbox('Plot Names'):
            plots = px.scatter(cdf, x=x_axis_val, y=y_axis_val, hover_name=cdf.Player, hover_data=['GP'],
                               title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val), text=cdf.Player)

        if st.button('Plot Chart'):
            st.plotly_chart(plots)
    else:
        plots = px.scatter(df2022, x=x_axis_val, y=y_axis_val, hover_name=df2022.Player, hover_data=['GP'],
                           title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val))

        if st.checkbox('Plot Names'):
            plots = px.scatter(df2022, x=x_axis_val, y=y_axis_val, hover_name=df2022.Player, hover_data=['GP'],
                               title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val), text=df2022.Player)

        if st.button('Plot Chart'):
            st.plotly_chart(plots)

if selected == "Stats Explained":
    
    st.title('Stats Explained')

    st.subheader('Paint PPG/PTS/FGA')
    st.write('Points and shots taken inside of the paint.')
    st.write(' ')
    st.write(' ')

    st.subheader('Paint FG%')
    st.write('FG% on shots taken inside the paint.')
    st.write(' ')
    st.write(' ')

    st.subheader('Paint rFG%')
    st.write('FG% on shots taken inside the paint minus the league average FG%.')
    st.write(' ')
    st.write(' ')

    st.subheader('Outside PPG/PTS/FGA')
    st.write('Points and shots taken outside of the paint.')
    st.write(' ')
    st.write(' ')

    st.subheader('Outside eFG%')
    st.write('eFG% on shots taken outside the paint.')
    st.write(' ')
    st.write(' ')

    st.subheader('Outside reFG%')
    st.write('eFG% on shots taken outside the paint minus the league average FG%.')
    st.write(' ')
    st.write(' ')

    st.subheader('Midrange PPG/PTS/FGA')
    st.write('All points and shots taken outside of the paint but not from three.')
    st.write(' ')
    st.write(' ')

    st.subheader('Midrange FG%')
    st.write('FG% on shots taken outside the paint but not from three.')
    st.write(' ')
    st.write(' ')

    st.subheader('Midrange rFG%')
    st.write('FG% on shots taken outside the paint but not from three minus the league average FG%.')
    st.write(' ')
    st.write(' ')