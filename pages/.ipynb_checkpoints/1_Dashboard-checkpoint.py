"""
Halaman Dashboard - Visualisasi Indikator Kinerja
"""

import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import KPI_DATA
from modules.analytics import (
    create_kpi_chart, 
    create_satisfaction_radar,
    create_processing_time_chart,
    create_trend_chart
)

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.title("📊 Dashboard Indikator Kinerja")
st.markdown("Visualisasi hasil penelitian sistem SKPI Digital berbasis Microservices")

st.markdown("---")

# ============================================================
# KPI METRICS
# ============================================================
st.subheader("🎯 Indikator Kinerja Utama (IKU)")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Waktu Proses", "↓73.1%", "7.8 → 2.1 hari")
with col2:
    st.metric("Test Coverage", "92.3%", ">90% target")
with col3:
    st.metric("UAT Satisfaction", "87.5%", ">85% target")
with col4:
    st.metric("Error Rate", "0.8%", "<1% target")
with col5:
    st.metric("Throughput", "78 req/s", ">50 target")

st.markdown("---")

# ============================================================
# CHARTS
# ============================================================
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(create_kpi_chart(KPI_DATA), use_container_width=True)

with col2:
    st.plotly_chart(create_satisfaction_radar(), use_container_width=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(create_processing_time_chart(), use_container_width=True)

with col2:
    st.plotly_chart(create_trend_chart(), use_container_width=True)

st.markdown("---")

# ============================================================
# TABEL KPI
# ============================================================
st.subheader("📋 Tabel Indikator Kinerja")

df_kpi = pd.DataFrame(KPI_DATA)
st.dataframe(df_kpi, use_container_width=True, hide_index=True)