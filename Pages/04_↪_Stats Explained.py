import streamlit as st
import pandas as pd

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