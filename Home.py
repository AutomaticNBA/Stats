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
        menu_title=None,
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
    #cdf2022 = pd.read_csv('./Files&Images/Yearly_Stats_2022.csv')

    st.title('Create Custom Player Charts')

    x_axis_val = st.selectbox('Select X-Axis', options=cdf.columns[4:20])
    y_axis_val = st.selectbox('Select Y-Axis', options=cdf.columns[4:20])

    st.write(' ')
    st.write(' ')


    year = st.selectbox(
        'Select A Season',
        ('Every Season', '2022', '2021', '2020', '2019', '2018', '2017',
         '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009',
         '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001',
         '2000', '1999', '1998', '1997')
    )



    # Allow to select players

    names = cdf['PlayerSansYear'].unique().tolist()


    with st.expander("Select up to 5 players"):

        p1 = st.selectbox('Select Player 1', names)

        p2 = st.selectbox('Select Player 2', names)

        p3 = st.selectbox('Select Player 3', names)

        p4 = st.selectbox('Select Player 4', names)

        p5 = st.selectbox('Select Player 5', names)

        if p1 or p2 or p3 or p4 or p5 in names:
            cdf = cdf[cdf['PlayerSansYear'] == p1, p2, p3, p4, p5]




    min_gp = st.slider("Minimum Games Played In A Season", 0, 82, 1)

    cdf = cdf[cdf['GP'] >= min_gp]

    st.write("Double click to reset chart")


    if year == "Every Season":
        plots = px.scatter(cdf, x=x_axis_val, y=y_axis_val, hover_name=cdf.Player, hover_data=['GP'],
                           title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val))

        if st.checkbox('Plot Names'):
            plots = px.scatter(cdf, x=x_axis_val, y=y_axis_val, hover_name=cdf.Player, hover_data=['GP'],
                               title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val), text=cdf.Player)

        if st.button('Plot Chart'):
            st.plotly_chart(plots)

    elif year == "2022":

        cdf = cdf[cdf['Year'] == 2022]

        plots = px.scatter(cdf, x=x_axis_val, y=y_axis_val, hover_name=cdf.Player, hover_data=['GP'],
                           title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val))

        if st.checkbox('Plot Names'):
            plots = px.scatter(cdf, x=x_axis_val, y=y_axis_val, hover_name=cdf.Player, hover_data=['GP'],
                               title=(year + ' ' + x_axis_val + ' ' + 'vs' + ' ' + y_axis_val), text=cdf.Player)

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