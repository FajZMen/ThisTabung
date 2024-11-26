import streamlit as st
from time import sleep as wait
import math

st.title("Welcome to Tabung Gajelas by Muhammad Fajar Shodiq")
st.write(
    "Di web, ini anda bisa Menghitung Volume Tabung! (VERYCOOL!)."
)

jarijari = st.number_input("Masukan jari-jari tabung: ",0)
panjang = st.number_input("Masukan panjang tabung: ",0)
justload = "Loading..."

if st.button("Hitung Volume", type="primary"):
    processing = st.progress(0, text=justload)
    for percent in range(100):
        wait(0.01)
        processing.progress(percent + 1, text=justload)
    wait(1)
    processing.empty()
    hasil = math.pi*(pow(jarijari,2))*panjang
    st.success(f"Volume Tabung: {hasil:.2f}")
