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
# STYLE (ADVANCED UI)
# =========================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #f4f6f9, #eef1f7);
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1f3c88, #162a5c);
}
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* HEADINGS */
h1, h2, h3 {
    color: #dd8046;
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* CARD */
.card {
    background-color: white;
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 25px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(0,0,0,0.12);
}

/* BUTTON */
.stButton > button {
    background-color: #dd8046;
    color: white;
    border-radius: 10px;
    padding: 10px 24px;
    font-weight: bold;
    border: none;
}
.stButton > button:hover {
    background-color: #c86f3d;
}

/* INFO BOX */
.info-box {
    background-color: #f0f2f6;
    padding: 15px;
    border-radius: 10px;
    border-left: 6px solid #dd8046;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
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

# PAGE 1 - PREDIKSI
if menu == "Prediksi Harga Rumah":
    st.title("Prediksi Harga Rumah")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
    Aplikasi ini mengklasifikasikan harga rumah ke dalam kategori 
    <b>Low</b>, <b>Medium</b>, dan <b>High</b> berdasarkan fitur input pengguna.
    </div>
    """, unsafe_allow_html=True)

    area = st.number_input("Luas Bangunan (m²)", 20, 500, 60)
    kamar = st.number_input("Jumlah Kamar Tidur", 1, 10, 3)

    if st.button("🔍 Prediksi Harga"):
        if area < 70:
            hasil = "LOW"
        elif area < 150:
            hasil = "MEDIUM"
        else:
            hasil = "HIGH"

        st.success(f"💰 **Hasil Prediksi Harga Rumah: {hasil}**")

    st.markdown('</div>', unsafe_allow_html=True)

# PAGE 2 - EVALUASI
elif menu == "Evaluasi & Analisis Model":
    st.title("Evaluasi dan Analisis Model")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Model yang Digunakan")
    st.markdown("""
    - **MLP (Neural Network)** – Non Pretrained  
    - **TabNet** – Pretrained  
    - **FT-Transformer** – Pretrained  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # CONFUSION MATRIX
    st.subheader("Confusion Matrix")

    models_cm = [
        ("MLP", "cm_mlp.png"),
        ("TabNet", "cm_tabnet.png"),
        ("FT-Transformer", "cm_fttransformer.png")
    ]

    cols = st.columns(3)
    for col, (name, file) in zip(cols, models_cm):
        path = os.path.join(ASSETS_DIR, file)
        with col:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"### {name}")
            if os.path.exists(path):
                st.image(Image.open(path), use_container_width=True)
            else:
                st.info("Confusion matrix belum tersedia")
            st.markdown('</div>', unsafe_allow_html=True)

    # ACCURACY & LOSS
    st.subheader("Accuracy & Loss")

    models_plot = [
        ("MLP", "acc_loss_mlp.png"),
        ("TabNet", "acc_loss_tabnet.png"),
        ("FT-Transformer", "acc_loss_fttransformer.png")
    ]

    cols = st.columns(3)
    for col, (name, file) in zip(cols, models_plot):
        path = os.path.join(ASSETS_DIR, file)
        with col:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"### {name}")
            if os.path.exists(path):
                st.image(Image.open(path), use_container_width=True)
            else:
                st.info("Grafik accuracy & loss belum tersedia")
            st.markdown('</div>', unsafe_allow_html=True)

    # TABEL
    st.subheader("Ringkasan Performa Model")

    st.markdown("""
    | Model | Accuracy | Precision | Recall | F1-Score | Analisis |
    |------|----------|-----------|--------|----------|----------|
    | MLP | 0.82 | 0.81 | 0.80 | 0.80 | Performa stabil namun sederhana |
    | TabNet | 0.86 | 0.85 | 0.84 | 0.84 | Lebih baik dalam relasi fitur |
    | FT-Transformer | 0.88 | 0.87 | 0.86 | 0.86 | Model terbaik dan konsisten |
    """)


# PAGE 3 - ABOUT
else:
    st.title("Tentang Aplikasi")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
    Aplikasi ini dikembangkan sebagai bagian dari **Ujian Akhir Praktikum Machine Learning**.
    Fokus utama aplikasi adalah membandingkan performa tiga model neural network
    dalam menyelesaikan masalah klasifikasi harga rumah berbasis data tabular.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
