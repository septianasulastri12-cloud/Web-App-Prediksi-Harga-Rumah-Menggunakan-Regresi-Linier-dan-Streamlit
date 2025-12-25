import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# =====================================================
# CONFIG PAGE
# =====================================================
st.set_page_config(
    page_title="Prediksi Harga Rumah",
    page_icon="🏠",
    layout="centered"
)

# =====================================================
# CUSTOM CSS (BIAR CANTIK)
# =====================================================
st.markdown("""
<style>
body {
    background-color: #f4f6fb;
}
.stApp {
    background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
}
h1, h2, h3 {
    color: #dd8046;
}
.css-1d391kg {
    background-color: #2c4fa1;
}
.stButton>button {
    background-color: #dd8046;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}
.stButton>button:hover {
    background-color: #c96f3f;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================
@st.cache_data
def load_data():
    df = pd.read_csv("D:\UAP-HOUSING\data\Housing.csv)
    return df

df = load_data()

# =====================================================
# PREPROCESSING
# =====================================================
X = df[["area", "bedrooms"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =====================================================
# TRAIN MODEL
# =====================================================
model = LinearRegression()
model.fit(X_train, y_train)

# =====================================================
# EVALUATION
# =====================================================
y_pred = model.predict(X_test)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred))
r2_lr = r2_score(y_test, y_pred)

# =====================================================
# SIDEBAR MENU
# =====================================================
st.sidebar.title("📌 Menu")
menu = st.sidebar.radio(
    "Pilih Halaman",
    ["🏠 Prediksi", "📊 Evaluasi Model", "ℹ️ Tentang Aplikasi"]
)

# =====================================================
# PAGE: PREDIKSI
# =====================================================
if menu == "🏠 Prediksi":
    st.title("🏠 Prediksi Harga Rumah")

    st.write("Masukkan spesifikasi rumah untuk memprediksi harga.")

    luas = st.number_input(
        "📐 Luas Rumah (m²)",
        min_value=20,
        max_value=1000,
        value=100
    )

    kamar = st.number_input(
        "🛏️ Jumlah Kamar Tidur",
        min_value=1,
        max_value=10,
        value=3
    )

    if st.button("🔍 Prediksi Harga"):
        input_data = [[luas, kamar]]
        prediksi = model.predict(input_data)[0]

        st.success(f"💰 Perkiraan Harga Rumah: Rp {prediksi:,.0f}")

        if prediksi < 300_000_000:
            st.info("📉 Kategori Harga: **Low**")
        elif prediksi < 700_000_000:
            st.info("📊 Kategori Harga: **Medium**")
        else:
            st.info("📈 Kategori Harga: **High**")

# =====================================================
# PAGE: EVALUASI
# =====================================================
elif menu == "📊 Evaluasi Model":
    st.title("📊 Evaluasi Model Regresi Linier")

    st.write("""
    Halaman ini menampilkan performa model regresi linier
    yang digunakan untuk memprediksi harga rumah.
    """)

    col1, col2 = st.columns(2)
    col1.metric("📉 RMSE", f"{rmse_lr:,.2f}")
    col2.metric("📈 R² Score", f"{r2_lr:.2f}")

    st.markdown("---")

    st.subheader("📌 Analisis Model")
    st.write("""
    - **RMSE** menunjukkan rata-rata kesalahan prediksi harga rumah.
    - **R² Score** menunjukkan seberapa baik model menjelaskan variasi data.
    
    Model ini cukup baik sebagai baseline dan cocok
    untuk implementasi sistem prediksi sederhana.
    """)

# =====================================================
# PAGE: ABOUT
# =====================================================
elif menu == "ℹ️ Tentang Aplikasi":
    st.title("ℹ️ Tentang Aplikasi")

    st.write("""
    **Web App Prediksi Harga Rumah** adalah sistem prediksi
    berbasis Machine Learning menggunakan Regresi Linier.
    """)

    st.markdown("---")

    st.subheader("📊 Dataset")
    st.write("""
    Dataset diambil dari Kaggle:
    *Housing Prices Dataset*
    
    Fitur yang digunakan:
    - Luas Rumah
    - Jumlah Kamar Tidur
    """)

    st.subheader("🧠 Model")
    st.write("""
    Model yang digunakan:
    - Linear Regression (Scikit-learn)
    """)

    st.subheader("👩‍💻 Dibuat oleh")
    st.write("""
    Nama Mahasiswa  
    NIM  
    Program Studi
    """)
