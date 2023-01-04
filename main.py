import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forcast for the Following Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperate", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

data = get_data(place, days, option)


d, t = get_data(days)

figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
