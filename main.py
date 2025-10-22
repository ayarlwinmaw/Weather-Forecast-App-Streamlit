import streamlit as st

st.title('Weather Forecast')
place = st.text_input('Enter your city name')
days = st.slider('Forecast Days', 1, 5,
                 help='Select number of days between 1 and 5')
option = st.selectbox("Select data to view",
                      (
                          "Temperature",
                          "Sky",
                          "Wind",
                          "Precipitation",
                      ))

st.subheader(f"{option} for the next {days} days in {place}")