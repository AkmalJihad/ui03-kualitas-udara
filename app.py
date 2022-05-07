import streamlit as st
import pickle

MODEL_FILE = "model.pkl" #Random Forest Classifier dengan akurasi 99%
pickle_in = open(MODEL_FILE, 'rb')
classifier = pickle.load(pickle_in)

st.set_page_config(
    page_title="ISPU",
    page_icon="☁️"
)

st.title("Indeks Standar Pencemar Udara V0.1")

st.subheader("Atur Parameter Variabel")

col1, col2, col3 = st.columns(3)

with col1:
     pm10 = st.slider('pm10: Partikulat', 0, 150, 30) 

with col2:
     pm25 = st.slider('pm25: Partikulat', 0, 150, 48) 

with col3:
     so2 = st.slider('so2: Sulfida', 0, 150, 24)
        
col4, col5, col6 = st.columns(3)

with col4:
     co = st.slider('co: Carbon Monoksida', 0, 150, 4)

with col5:
     o3 = st.slider('o3: Ozon', 0, 150, 32)

with col6:
     no2 = st.slider('no2: Nitrogen dioksida', 0, 150, 7)

st.subheader("Kualitas udara sekarang:")
prediction = classifier.predict([[pm10, pm25, so2, co, o3, no2]])
if (prediction[0] == 0) :
    st.success("Baik")
elif (prediction[0] == 1) :
    st.success("Sedang")
elif (prediction[0] == 2) :
    st.success("Tidak Sehat")
