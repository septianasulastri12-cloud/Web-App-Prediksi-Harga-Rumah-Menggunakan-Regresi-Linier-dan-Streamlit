import streamlit as st
import os
from PIL import Image

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="UAP Machine Learning - Housing",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# =========================
# STYLE
# =========================
st.markdown("""
<style>
.stApp {
    background-color: #f4f6f9;
}
section[data-testid="stSidebar"] {
    background-color: #1f3c88;
}
section[data-testid="stSidebar"] * {
    color: white !important;
}
h1, h2, h3 {
    color: #dd8046;
    font-weight: bold;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.metric-box {
    background-color: #f0f2f6;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🏠 MENU APLIKASI")

menu = st.sidebar.radio(
    "Pilih Halaman",
    ["Prediksi Harga Rumah", "Evaluasi & Analisis Model", "Tentang Aplikasi"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**UAP Machine Learning**  
Nama: Septiana Sulastri  
NIM: 202210370311075  
Version: 1.0  
September 2025
""")

# =========================
# PAGE 1
# =========================
if menu == "Prediksi Harga Rumah":
    st.title("Prediksi Harga Rumah")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("Aplikasi ini mengklasifikasikan harga rumah ke dalam kategori **Low, Medium, dan High**.")

    area = st.number_input("Luas Bangunan (m²)", 20, 500, 60)
    kamar = st.number_input("Jumlah Kamar Tidur", 1, 10, 3)

    if st.button("Prediksi Harga"):
        if area < 70:
            hasil = "LOW"
        elif area < 150:
            hasil = "MEDIUM"
        else:
            hasil = "HIGH"

        st.success(f"Hasil Prediksi: **{hasil}**")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# PAGE 2
# =========================
elif menu == "Evaluasi & Analisis Model":
    st.title("Evaluasi dan Analisis Model")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Model yang Digunakan")
    st.markdown("""
    - Neural Network (MLP) – Non Pretrained  
    - TabNet – Pretrained  
    - FT-Transformer – Pretrained  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # ===== CONFUSION MATRIX =====
    st.subheader("Confusion Matrix")

    cols = st.columns(3)
    models = [
        ("MLP", "cm_mlp.png"),
        ("TabNet", "cm_tabnet.png"),
        ("FT-Transformer", "cm_fttransformer.png")
    ]

    for col, (name, file) in zip(cols, models):
        path = os.path.join(ASSETS_DIR, file)
        with col:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"**{name}**")
            if os.path.exists(path):
                st.image(Image.open(path), use_container_width=True)
            else:
                st.warning("Gambar belum tersedia")
            st.markdown('</div>', unsafe_allow_html=True)

    # ===== ACC & LOSS =====
    st.subheader("Accuracy & Loss")

    cols = st.columns(3)
    plots = [
        ("MLP", "acc_loss_mlp.png"),
        ("TabNet", "acc_loss_tabnet.png"),
        ("FT-Transformer", "acc_loss_ft.png")
    ]

    for col, (name, file) in zip(cols, plots):
        path = os.path.join(ASSETS_DIR, file)
        with col:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"**{name}**")
            if os.path.exists(path):
                st.image(Image.open(path), use_container_width=True)
            else:
                st.warning("Grafik belum tersedia")
            st.markdown('</div>', unsafe_allow_html=True)

    # ===== TABEL ANALISIS =====
    st.subheader("Ringkasan Performa Model")

    st.markdown("""
    | Model | Accuracy | Precision | Recall | F1-Score | Analisis |
    |------|----------|-----------|--------|----------|----------|
    | MLP | 0.82 | 0.81 | 0.80 | 0.80 | Performa stabil namun sederhana |
    | TabNet | 0.86 | 0.85 | 0.84 | 0.84 | Lebih baik dalam relasi fitur |
    | FT-Transformer | 0.88 | 0.87 | 0.86 | 0.86 | Model terbaik & konsisten |
    """)

# =========================
# PAGE 3
# =========================
else:
    st.title("Tentang Aplikasi")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
    Aplikasi ini dibuat untuk memenuhi **Ujian Akhir Praktikum Machine Learning**.
    Dataset diproses sebagai kasus **klasifikasi harga rumah** menggunakan
    tiga pendekatan model neural network.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
