import streamlit as st
import pickle

MODEL_FILE = "model.pkl"
pickle_in = open(MODEL_FILE, 'rb')
classifier = pickle.load(pickle_in)

st.set_page_config(
    page_title="ISPU",
    page_icon="☁️"
)

st.title("Indeks Standar Pencemar Udara")
st.caption("Random Forest Classifier")

st.subheader("Parameter")

col1, col2, col3 = st.columns(3)

with col1:
     pm10 = st.number_input('PM10', 0, 500) 

with col2:
     pm25 = st.number_input('PM2.5', 0, 500) 

with col3:
     so2 = st.number_input('SO2', 0, 1200) 
        
col4, col5, col6 = st.columns(3)

with col4:
     co = st.number_input('CO', 0, 45000) 

with col5:
     o3 = st.number_input('O3', 0, 1000) 

with col6:
     no2 = st.number_input('NO2', 0, 3000) 

st.subheader("Kategori ISPU:")
prediction = classifier.predict([[pm10, pm25, so2, co, o3, no2]])
if (prediction[0] == 0) :
    st.success("Baik")
elif (prediction[0] == 1) :
    st.success("Sedang")
elif (prediction[0] == 2) :
    st.success("Tidak Sehat")
