import streamlit as st

st.title("Prediksi Harga Rumah")

luas = st.number_input("Luas Rumah (m2)", min_value=0)
kamar = st.number_input("Jumlah Kamar", min_value=0)

if st.button("Prediksi"):
    st.success("Harga Rumah: Rp 350.000")
    st.info("Kategori: Medium")
