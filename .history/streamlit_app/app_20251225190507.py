import streamlit as st

# ===============================
# KONFIGURASI HALAMAN
# ===============================
st.set_page_config(
    page_title="Prediksi Harga Rumah",
    page_icon="🏠",
    layout="centered"
)

# ===============================
# SIDEBAR
# ===============================
st.sidebar.title("🏠 Menu Aplikasi")
menu = st.sidebar.radio(
    "Pilih Halaman:",
    ["Prediksi Harga Rumah", "Tentang Model", "Tentang Aplikasi"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "UAP Machine Learning\n\n"
    "Nama: (ISI NAMAMU)\n"
    "NIM: (ISI NIM)\n"
    "Kelas: (ISI KELAS)"
)

# ===============================
# HALAMAN 1: PREDIKSI
# ===============================
if menu == "Prediksi Harga Rumah":
    st.title("🏠 Prediksi Harga Rumah")
    st.markdown(
        """
        Aplikasi ini digunakan untuk **memprediksi harga rumah**
        berdasarkan beberapa fitur menggunakan **Machine Learning**.
        """
    )

    st.markdown("### 📝 Input Data Rumah")

    col1, col2 = st.columns(2)

    with col1:
        luas = st.number_input(
            "Luas Rumah (m²)",
            min_value=10,
            step=1
        )

    with col2:
        kamar = st.number_input(
            "Jumlah Kamar",
            min_value=1,
            step=1
        )

    st.markdown("---")

    if st.button("🔍 Prediksi Harga", use_container_width=True):
        # -------------------------------
        # DUMMY OUTPUT (NANTI GANTI MODEL)
        # -------------------------------
        harga_prediksi = 350_000

        if harga_prediksi < 200_000:
            kategori = "Low"
            warna = "🟢"
        elif harga_prediksi < 500_000:
            kategori = "Medium"
            warna = "🟡"
        else:
            kategori = "High"
            warna = "🔴"

        st.success(f"💰 **Harga Rumah:** Rp {harga_prediksi:,.0f}")
        st.info(f"{warna} **Kategori Harga:** {kategori}")

# ===============================
# HALAMAN 2: TENTANG MODEL
# ===============================
elif menu == "Tentang Model":
    st.title("📊 Tentang Model")

    st.markdown(
        """
        Pada proyek ini digunakan beberapa model Machine Learning, yaitu:
        """
    )

    st.markdown("#### 1️⃣ Regresi Linier")
    st.write(
        "Digunakan sebagai **baseline model** sesuai dengan judul proyek "
        "untuk memprediksi harga rumah secara langsung."
    )

    st.markdown("#### 2️⃣ Neural Network (MLP)")
    st.write(
        "Model **Multilayer Perceptron (MLP)** digunakan untuk meningkatkan "
        "akurasi prediksi dibandingkan regresi linier."
    )

    st.markdown("#### 3️⃣ Evaluasi Model")
    st.write(
        "Hasil prediksi harga dikonversi menjadi **kategori harga** "
        "(Low, Medium, High) agar dapat dievaluasi menggunakan "
        "Classification Report dan Confusion Matrix."
    )

# ===============================
# HALAMAN 3: TENTANG APLIKASI
# ===============================
elif menu == "Tentang Aplikasi":
    st.title("ℹ️ Tentang Aplikasi")

    st.markdown(
        """
        **Web App Prediksi Harga Rumah**  
        
        Aplikasi ini dibuat untuk memenuhi tugas **Ujian Akhir Praktikum (UAP)**
        pada mata kuliah Machine Learning.
        """
    )

    st.markdown("### 🎯 Tujuan")
    st.write(
        "Membangun sistem prediksi harga rumah berbasis Machine Learning "
        "yang dapat digunakan secara interaktif melalui web."
    )

    st.markdown("### 🛠️ Teknologi yang Digunakan")
    st.markdown(
        """
        - Python  
        - Scikit-Learn  
        - Streamlit  
        """
    )

    st.markdown("### 📌 Catatan")
    st.info(
        "Aplikasi ini dijalankan secara lokal menggunakan Streamlit "
        "dan digunakan sebagai media demonstrasi model."
    )
