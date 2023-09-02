import streamlit as st
st.title("AIR Quality Prediction")
import pickle

category = {'Good':0, 'Hazardous':1, 'Moderate':2, 'Unhealthy':3,
 'Unhealthy for Sensitive Groups':4, 'Very Unhealthy':5}

def status(AQI_value):
    if AQI_value <= 50:
        return "Good"
    elif AQI_value <= 100:
        return "Moderate"
    elif AQI_value <= 150:
        return "Unhealthy for Sensitive Groups"   
    elif AQI_value <= 200:
        return "Unhealthy"
    elif AQI_value <= 300:
        return "Very Unhealthy"
    elif AQI_value > 300:
        return "Hazardous" 

CO_aqival = st.number_input("CO AQI Value", min_value = 0, max_value = 500)
Ozone_aqival = st.number_input("Ozone AQI Value", min_value=0, max_value = 500)
NO2_aqival = st.number_input("NO2 AQI Value", min_value=0, max_value = 500)
PM25_aqival = st.number_input("PM2.5 AQI Value", min_value=0, max_value = 500)

CO_aqicat = status(CO_aqival)
Ozone_aqicat = status(Ozone_aqival)
NO2_aqicat = status(NO2_aqival)
PM25_aqicat = status(PM25_aqival)

button = st.button("Predict")
if button:
    with open('pickle_model.pickle', 'rb') as f:
        model = pickle.load(f)
        prediction = model.predict([[CO_aqival, category[CO_aqicat], Ozone_aqival, category[Ozone_aqicat], NO2_aqival, category[NO2_aqicat], PM25_aqival,
                                      category[PM25_aqicat]]])
        st.write("AQI value :", prediction)
        st.write("AIR STATUS :", status(prediction))