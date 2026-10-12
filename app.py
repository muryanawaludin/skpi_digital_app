"""
SKPI Digital - Microservices System
Main Streamlit Application
"""

import streamlit as st
import pandas as pd
import sys
import os

# Tambahkan path untuk import modul
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config.settings import APP_TITLE, APP_ICON, UNIVERSITY, FACULTY
from utils.database import db

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #3498DB;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #7F8C8D;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #3498DB 0%, #2980B9 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
    }
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .stButton>button {
        background-color: #3498DB;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #2980B9;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=UNSURYA", width=150)
    st.title("🎓 SKPI Digital")
    st.markdown(f"**{UNIVERSITY}**")
    st.markdown(f"*{FACULTY}*")
    st.markdown("---")
    
    st.markdown("### 📌 Navigasi")
    st.markdown("""
    - 📊 **Dashboard** - Visualisasi IKU
    - 📝 **Input Capaian** - Input prestasi
    - ✅ **Verifikasi SKPI** - Validasi dokumen
    - 📈 **Monitoring System** - Performa sistem
    - 👥 **Data Mahasiswa** - Database mahasiswa
    """)
    
    st.markdown("---")
    st.markdown("### ℹ️ Informasi")
    st.info("""
    **Microservices Architecture**
    - Student Service
    - Achievement Service
    - Document Service
    - Verification Service
    """)

# ============================================================
# HALAMAN UTAMA
# ============================================================
st.markdown('<div class="main-header">🎓 SKPI Digital System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Microservices-Based Academic Service Platform</div>', unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# RINGKASAN INDIKATOR KINERJA
# ============================================================
st.subheader("📊 Ringkasan Indikator Kinerja Utama")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="⏱️ Waktu Proses SKPI",
        value="↓73.1%",
        delta="7.8 → 2.1 hari"
    )

with col2:
    st.metric(
        label="😊 Kepuasan Pengguna",
        value="4.3/5.0",
        delta="+1.5 dari baseline"
    )

with col3:
    st.metric(
        label="⚡ Response Time",
        value="156 ms",
        delta="-44 ms dari target"
    )

with col4:
    st.metric(
        label="📉 Error Rate",
        value="0.8%",
        delta="-7.2% dari baseline"
    )

st.markdown("---")

# ============================================================
# TENTANG APLIKASI
# ============================================================
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📖 Tentang Aplikasi")
    st.markdown("""
    Aplikasi **SKPI Digital** ini merupakan implementasi dari penelitian 
    **"Pengembangan Sistem SKPI Digital dengan Arsitektur Microservices dan API Gateway"** 
    yang dikembangkan untuk:
    
    1. **Mempercepat** proses penerbitan SKPI dari 7.8 hari menjadi 2.1 hari
    2. **Meningkatkan** akurasi data melalui validasi otomatis
    3. **Memudahkan** integrasi dengan sistem eksternal (SIAKAD, industri)
    4. **Menyediakan** portofolio kompetensi lulusan yang terverifikasi
    
    ### 🏗️ Arsitektur Microservices
    
    Aplikasi ini terdiri dari 4 layanan utama:
    
    | Layanan | Fungsi | Teknologi |
    |:--------|:-------|:----------|
    | **Student Service** | Manajemen data mahasiswa | PostgreSQL |
    | **Achievement Service** | Pencatatan capaian | PostgreSQL |
    | **Document Service** | Generate SKPI + QR Code | MongoDB |
    | **Verification Service** | Validasi dokumen | PostgreSQL |
    """)

with col2:
    st.subheader("📈 Statistik Populasi")
    
    students = db.get_all_students()
    st.metric("Total Mahasiswa", len(students))
    st.metric("Program Studi", students['PRODI'].nunique())
    st.metric("Angkatan", students['ANGKATAN'].nunique())
    
    st.markdown("---")
    st.markdown("### 🚀 Fitur Utama")
    st.success("✅ Input capaian mandiri")
    st.success("✅ Validasi 2 tahap")
    st.success("✅ QR Code verification")
    st.success("✅ Real-time monitoring")

st.markdown("---")

# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div style="text-align: center; color: #7F8C8D; padding: 2rem;">
    <p>© 2026 - Fakultas Ilmu Komputer dan Desain</p>
    <p>Universitas Dirgantara Marsekal Suryadarma</p>
    <p><em>Microservices-Based SKPI Digital System v1.0</em></p>
</div>
""", unsafe_allow_html=True)