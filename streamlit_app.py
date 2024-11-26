import streamlit as st

st.title("Welcome to Tabung Gajelas")
st.write(
    "Di web ini anda bisa Menghitung Tabung (VERY COOL!)."
)

jarijari = st.number_input("Masukan jari-jari tabung: ",0)
panjang = st.number_input("Masukan panjang tabung: ",0)
