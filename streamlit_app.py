import streamlit as st

st.title("Welcome to Tabung Gajelas")
st.write(
    "Di web ini anda bisa Menghitung Tabung (VERY COOL!)."
)

jarijari = st.number_input("Masukan jari-jari tabung: ",0)
panjang = st.number_input("Masukan panjang tabung: ",0)

if st.buttot("Hitung Volume", type="primary"):
    hasil = math.pi*(pow(jarijari,2))*panjang
    st.success(f"Volume Tabung: {hasil:.2f}")
