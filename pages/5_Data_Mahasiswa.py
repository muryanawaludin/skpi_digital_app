"""
Halaman Data Mahasiswa
"""

import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.database import db

st.set_page_config(page_title="Data Mahasiswa", page_icon="👥", layout="wide")

st.title("👥 Data Mahasiswa FIKD Unsurya")
st.markdown("Database mahasiswa Program Studi Informatika & Sistem Informasi")

st.markdown("---")

# ============================================================
# STATISTIK
# ============================================================
students = db.get_all_students()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Mahasiswa", len(students))
with col2:
    st.metric("Program Studi", students['PRODI'].nunique())
with col3:
    st.metric("Angkatan", students['ANGKATAN'].nunique())
with col4:
    st.metric("Jalur Masuk", students['JALUR'].nunique())

st.markdown("---")

# ============================================================
# FILTER
# ============================================================
st.subheader("🔍 Filter Data")

col1, col2, col3 = st.columns(3)

with col1:
    prodi_filter = st.multiselect(
        "Program Studi",
        options=students['PRODI'].unique(),
        default=students['PRODI'].unique()
    )

with col2:
    angkatan_filter = st.multiselect(
        "Angkatan",
        options=students['ANGKATAN'].unique(),
        default=students['ANGKATAN'].unique()
    )

with col3:
    jalur_filter = st.multiselect(
        "Jalur Masuk",
        options=students['JALUR'].unique(),
        default=students['JALUR'].unique()
    )

# Apply filter
filtered = students[
    (students['PRODI'].isin(prodi_filter)) &
    (students['ANGKATAN'].isin(angkatan_filter)) &
    (students['JALUR'].isin(jalur_filter))
]

st.markdown("---")

# ============================================================
# TABEL DATA
# ============================================================
st.subheader(f"📋 Data Mahasiswa ({len(filtered)} records)")

st.dataframe(filtered, use_container_width=True, hide_index=True)

# Download button
csv = filtered.to_csv(index=False).encode('utf-8')
st.download_button(
    "📥 Download CSV",
    data=csv,
    file_name="data_mahasiswa.csv",
    mime="text/csv",
    use_container_width=True
)

# ============================================================
# COPYRIGHT Muryan Awaludin
# ============================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7F8C8D; font-size: 0.8rem; padding: 1rem 0;">
    <p>© 2026 <strong>Muryan Awaludin</strong> | SKPI Digital System v1.0</p>
    <p>Universitas Dirgantara Marsekal Suryadarma</p>
</div>
""", unsafe_allow_html=True)