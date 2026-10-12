"""
Halaman Verifikasi SKPI dengan QR Code
"""

import streamlit as st
from PIL import Image
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.database import db
from utils.qr_generator import generate_qr_code, qr_to_bytes

st.set_page_config(page_title="Verifikasi SKPI", page_icon="✅", layout="wide")

st.title("✅ Verifikasi Dokumen SKPI")
st.markdown("Halaman untuk generate dan verifikasi dokumen SKPI dengan QR Code")

st.markdown("---")

# ============================================================
# GENERATE DOKUMEN
# ============================================================
st.subheader("📄 Generate Dokumen SKPI")

col1, col2 = st.columns([1, 2])

with col1:
    nim = st.selectbox(
        "Pilih Mahasiswa",
        options=db.get_all_students()['NIM'].tolist()
    )
    
    if st.button("🔄 Generate SKPI", use_container_width=True):
        doc = db.generate_document(nim)
        st.success(f"✅ Dokumen {doc['ID_DOKUMEN']} berhasil dibuat!")
        st.session_state['last_doc'] = doc

with col2:
    if 'last_doc' in st.session_state:
        doc = st.session_state['last_doc']
        student = db.get_student(doc['NIM'])
        
        st.markdown(f"""
        **ID Dokumen:** {doc['ID_DOKUMEN']}  
        **Nama:** {student['NAMA']}  
        **NIM:** {student['NIM']}  
        **Tanggal Terbit:** {doc['TANGGAL_TERBIT']}  
        **Status:** {doc['STATUS']}
        """)
        
        # Generate QR Code
        qr_img = generate_qr_code(doc['QR_CODE'], size=200)
        st.image(qr_img, caption="QR Code Verifikasi", width=200)

st.markdown("---")

# ============================================================
# VERIFIKASI DOKUMEN
# ============================================================
st.subheader("🔍 Verifikasi Dokumen")

doc_id = st.text_input("Masukkan ID Dokumen", placeholder="Contoh: SKPI0001")

if st.button("🔎 Verifikasi", use_container_width=True):
    if doc_id:
        result = db.verify_document(doc_id)
        
        if result['valid']:
            st.success("✅ Dokumen VALID")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 👤 Data Mahasiswa")
                st.json(result['student'])
            
            with col2:
                st.markdown("### 📋 Capaian Terverifikasi")
                st.metric("Total Capaian", result['total_achievements'])
                if result['achievements']:
                    st.dataframe(
                        result['achievements'],
                        use_container_width=True,
                        hide_index=True
                    )
        else:
            st.error(f"❌ {result['message']}")
    else:
        st.warning("⚠️ Masukkan ID Dokumen terlebih dahulu")