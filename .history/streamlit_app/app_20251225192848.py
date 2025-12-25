import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Prediksi Harga Rumah",
    layout="wide"
)

# ==============================
# STYLE GUIDE (CSS)
# ==============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

html, body, [class*="css"] {
    font-family: 'Roboto', sans-serif;
    font-size: 11px;
    color: black;
}

/* Background */
.stApp {
    background-color: #f7f9fc;
}

/* HEADINGS */
h1 {
    font-size: 14px;
    font-weight: bold;
    color: #dd8046;
    text-transform: uppercase;
}

h2 {
    font-size: 12px;
    font-weight: bold;
    color: #dd8046;
    text-transform: uppercase;
}

h3 {
    font-size: 12px;
    font-weight: bold;
    color: #dd8046;
    text-transform: uppercase;
}

/* LINK */
a {
    color: blue;
    text-decoration: underline;
}

/* TABLE */
table {
    width: 100%;
    border-collapse: collapse;
    font-size: 11px;
}

th {
    background-color: #2c4fa1;
    color: white;
    padding: 8px;
    text-align: center;
}

td {
    padding: 8px;
    border: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# LOAD DATA
# ==============================
@st.cache_data
def load_data():
    df = pd.read_csv("data/Housing.csv")
    return df

df = load_data()

# ==============================
# PREPROCESSING
# ==============================
features = ["area", "bedrooms"]
target = "price"

X = df[features]
y = df[target]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ==============================
# MODEL (NON-PRETRAINED NN)
# ==============================
model = MLPRegressor(
    hidden_layer_sizes=(64, 32),
    max_iter=500,
    random_state=42
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# ==============================
# SIDEBAR MENU
# ==============================
st.sidebar.markdown("## 🏠 Menu Aplikasi")
menu = st.sidebar.radio(
    "Pilih Halaman:",
    ["Prediksi Harga Rumah", "Evaluasi Model", "Tentang Aplikasi"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**UAP Machine Learning**  
Nama: Septiana Sulastri  
NIM: 202210370311075  
Version: 1.0  
Approved: September 2025
""")

# ==============================
# PAGE: PREDIKSI
# ==============================
if menu == "Prediksi Harga Rumah":
    st.markdown("<h1>Prediksi Harga Rumah</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p>
    Aplikasi ini digunakan untuk memprediksi harga rumah
    menggunakan model Neural Network (MLP).
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<h2>Input Data Rumah</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        area = st.number_input("Luas Rumah (m²)", min_value=10, value=50)
    with col2:
        bedrooms = st.number_input("Jumlah Kamar", min_value=1, value=2)

    if st.button("🔍 Prediksi Harga"):
        input_data = scaler.transform([[area, bedrooms]])
        prediction = model.predict(input_data)[0]

        st.success(f"💰 Perkiraan Harga Rumah: Rp {prediction:,.0f}")

# ==============================
# PAGE: EVALUASI
# ==============================
elif menu == "Evaluasi Model":
    st.markdown("<h1>Evaluasi Model</h1>", unsafe_allow_html=True)

    st.markdown("<h2>Metode Evaluasi</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p>
    Evaluasi dilakukan menggunakan RMSE dan R-Squared
    untuk mengukur performa model regresi.
    </p>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <table>
    <tr>
        <th>Metric</th>
        <th>Nilai</th>
    </tr>
    <tr>
        <td>RMSE</td>
        <td>{rmse:.2f}</td>
    </tr>
    <tr>
        <td>R-Squared</td>
        <td>{r2:.2f}</td>
    </tr>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("<h2>Visualisasi Prediksi</h2>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.set_xlabel("Harga Aktual")
    ax.set_ylabel("Harga Prediksi")
    st.pyplot(fig)

# ==============================
# PAGE: TENTANG
# ==============================
else:
    st.markdown("<h1>Tentang Aplikasi</h1>", unsafe_allow_html=True)

    st.markdown("""
    <p>
    Aplikasi ini dikembangkan sebagai bagian dari
    <b>Ujian Akhir Praktikum Machine Learning</b>.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3>Dataset</h3>
    <a href="https://www.kaggle.com/datasets/yasserh/housing-prices-dataset" target="_blank">
    LINK-DATASET_HOUSING
    </a>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3>Model</h3>
    <p>
    Model yang digunakan adalah Neural Network
    (Multilayer Perceptron) yang dibangun dari awal
    tanpa pretrained model.
    </p>
    """, unsafe_allow_html=True)
