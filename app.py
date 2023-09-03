import streamlit as st
import pickle
from playsound import playsound
import subprocess
st.title("AIR Quality Prediction")


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

CO_aqival = st.slider("CO AQI Value", 0, 500)
Ozone_aqival = st.slider("Ozone AQI Value", 0, 500)
NO2_aqival = st.slider("NO2 AQI Value", 0, 500)
PM25_aqival = st.slider("PM2.5 AQI Value", 0, 500)

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
        if status(prediction) == "Very Unhealthy" or status(prediction) == "Hazardous" :
            st.warning('This is dangerous', icon="⚠️")
            audio_file = st.file_uploader("alert.mp3", type=["mp3", "wav"])
            st.markdown(f'<audio controls src="data:audio/{audio_file.type};base64,{audio_file.read().decode("utf-8")}"></audio>', unsafe_allow_html=True)
