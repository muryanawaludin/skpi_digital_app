"""
Halaman Input Capaian Mahasiswa
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.database import db

st.set_page_config(page_title="Input Capaian", page_icon="📝", layout="wide")

st.title("📝 Input Capaian Mahasiswa")
st.markdown("Formulir untuk menginput capaian akademik dan non-akademik")

st.markdown("---")

# ============================================================
# FORM INPUT
# ============================================================
with st.form("form_capaian"):
    col1, col2 = st.columns(2)
    
    with col1:
        nim = st.selectbox(
            "NIM Mahasiswa",
            options=db.get_all_students()['NIM'].tolist(),
            help="Pilih NIM mahasiswa"
        )
        
        jenis = st.selectbox(
            "Jenis Capaian",
            options=["Sertifikasi", "Kompetisi", "Organisasi", "Pelatihan", "Publikasi"]
        )
        
        tingkat = st.selectbox(
            "Tingkat",
            options=["Internasional", "Nasional", "Regional", "Universitas", "Fakultas"]
        )
    
    with col2:
        nama_kegiatan = st.text_input(
            "Nama Kegiatan",
            placeholder="Contoh: Juara 1 Hackathon Nasional 2025"
        )
        
        tanggal = st.date_input(
            "Tanggal Kegiatan",
            value=datetime.now()
        )
        
        file_upload = st.file_uploader(
            "Upload Sertifikat (PDF/JPG)",
            type=['pdf', 'jpg', 'jpeg', 'png']
        )
    
    submitted = st.form_submit_button("💾 Simpan Capaian", use_container_width=True)
    
    if submitted:
        if not nama_kegiatan:
            st.error("❌ Nama kegiatan harus diisi!")
        else:
            result = db.add_achievement(
                nim=nim,
                jenis=jenis,
                nama_kegiatan=nama_kegiatan,
                tingkat=tingkat,
                tanggal=tanggal.strftime('%Y-%m-%d')
            )
            st.success(f"✅ Capaian berhasil disimpan! ID: {result['ID']}")
            st.balloons()

st.markdown("---")

# ============================================================
# DAFTAR CAPAIAN
# ============================================================
st.subheader("📋 Daftar Capaian Tersimpan")

achievements = db.get_achievements()

if achievements.empty:
    st.info("Belum ada capaian yang tersimpan.")
else:
    st.dataframe(achievements, use_container_width=True, hide_index=True)
    
    # Statistik
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Capaian", len(achievements))
    with col2:
        st.metric("Pending", len(achievements[achievements['STATUS'] == 'Pending']))
    with col3:
        st.metric("Approved", len(achievements[achievements['STATUS'] == 'Approved']))