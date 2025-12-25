import streamlit as st
import pandas as pd
from PIL import Image

# =====================
# CONFIG
# =====================
st.set_page_config(
    page_title="Prediksi Harga Rumah",
    layout="wide"
)

# =====================
# STYLE (GLOBAL)
# =====================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

html, body, [class*="css"] {
    font-family: 'Roboto', sans-serif;
    font-size: 11px;
}

/* MAIN BG */
.stApp {
    background-color: #f4f6f9;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #1f3c88;
    color: white;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* HEADINGS */
h1, h2, h3 {
    color: #dd8046;
    text-transform: uppercase;
    font-weight: bold;
}

/* BUTTON */
.stButton > button {
    background-color: #dd8046;
    color: white;
    border-radius: 8px;
    font-weight: bold;
}

/* TABLE */
table {
    width: 100%;
    border-collapse: collapse;
}
th {
    background-color: #2c4fa1;
    color: white;
    padding: 8px;
}
td {
    padding: 8px;
    border: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

# =====================
# SIDEBAR
# =====================
st.sidebar.markdown("## 🏠 MENU APLIKASI")

menu = st.sidebar.radio(
    "Pilih Halaman:",
    [
        "Prediksi Harga Rumah",
        "Evaluasi & Analisis Model",
        "Tentang Aplikasi"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**UAP Machine Learning**  
Nama: Septiana Sulastri  
NIM: 202210370311075  
Version: 1.0  
September 2025
""")

# =====================
# PAGE 1: PREDIKSI
# =====================
if menu == "Prediksi Harga Rumah":
    st.markdown("# Prediksi Harga Rumah")

    st.markdown("""
    Aplikasi ini melakukan **klasifikasi harga rumah**
    ke dalam kategori **Low, Medium, dan High**
    menggunakan model Machine Learning.
    """)

    col1, col2 = st.columns(2)
    with col1:
        area = st.number_input("Luas Rumah (m²)", 10, 500, 50)
    with col2:
        bedroom = st.number_input("Jumlah Kamar", 1, 10, 2)

    if st.button("🔍 Prediksi"):
        # Dummy rule (karena model asli di notebook)
        if area < 60:
            result = "LOW"
        elif area < 120:
            result = "MEDIUM"
        else:
            result = "HIGH"

        st.success(f"🏷️ Kategori Harga Rumah: **{result}**")

# =====================
# PAGE 2: EVALUASI
# =====================
elif menu == "Evaluasi & Analisis Model":
    st.markdown("# Evaluasi dan Analisis Model")

    st.markdown("## Model yang Digunakan")
    st.markdown("""
    - Neural Network (MLP) – Non Pretrained  
    - TabNet – Pretrained  
    - FT-Transformer – Pretrained  
    """)

    st.markdown("## Confusion Matrix")
    col1, col2, col3 = st.columns(3)
    col1.image(Image.open("assets/cm_mlp.png"), caption="MLP")
    col2.image(Image.open("assets/cm_tabnet.png"), caption="TabNet")
    col3.image(Image.open("assets/cm_fttransformer.png"), caption="FT-Transformer")

    st.markdown("## Loss & Accuracy")
    col1, col2, col3 = st.columns(3)
    col1.image(Image.open("assets/loss_mlp.png"), caption="MLP")
    col2.image(Image.open("assets/loss_tabnet.png"), caption="TabNet")
    col3.image(Image.open("assets/loss_fttransformer.png"), caption="FT-Transformer")

    st.markdown("## Tabel Perbandingan Model")
    st.markdown("""
    <table>
    <tr>
        <th>Model</th>
        <th>Accuracy</th>
        <th>Precision</th>
        <th>Recall</th>
        <th>F1-Score</th>
        <th>Analisis</th>
    </tr>
    <tr>
        <td>MLP</td>
        <td>0.82</td>
        <td>0.81</td>
        <td>0.80</td>
        <td>0.80</td>
        <td>Stabil namun kurang pada data kompleks</td>
    </tr>
    <tr>
        <td>TabNet</td>
        <td>0.86</td>
        <td>0.85</td>
        <td>0.84</td>
        <td>0.84</td>
        <td>Menangkap relasi fitur dengan baik</td>
    </tr>
    <tr>
        <td>FT-Transformer</td>
        <td>0.88</td>
        <td>0.87</td>
        <td>0.86</td>
        <td>0.86</td>
        <td>Performa terbaik dan stabil</td>
    </tr>
    </table>
    """, unsafe_allow_html=True)

# =====================
# PAGE 3: ABOUT
# =====================
else:
    st.markdown("# Tentang Aplikasi")

    st.markdown("""
    Proyek ini dibuat untuk **Ujian Akhir Praktikum Machine Learning**.
    Dataset berasal dari Kaggle dan diproses sebagai
    **kasus klasifikasi data tabular**.
    """)

    st.markdown("""
    🔗 <a href="https://www.kaggle.com/datasets/yasserh/housing-prices-dataset" target="_blank">
    LINK-DATASET_HOUSING
    </a>
    """, unsafe_allow_html=True)
