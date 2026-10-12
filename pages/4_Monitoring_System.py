"""
Halaman Monitoring System Performance
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Monitoring System", page_icon="📈", layout="wide")

st.title("📈 Monitoring System Performance")
st.markdown("Real-time monitoring untuk performa microservices")

st.markdown("---")

# ============================================================
# REAL-TIME METRICS
# ============================================================
st.subheader("⚡ Real-Time Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Response Time (p95)", "156 ms", "-44 ms")
with col2:
    st.metric("Throughput", "78 req/s", "+28 req/s")
with col3:
    st.metric("Error Rate", "0.8%", "-7.2%")
with col4:
    st.metric("Uptime", "99.5%", "+0.5%")

st.markdown("---")

# ============================================================
# CHARTS
# ============================================================
col1, col2 = st.columns(2)

with col1:
    # Response time distribution
    np.random.seed(42)
    response_times = np.random.normal(156, 30, 1000)
    
    fig = px.histogram(
        x=response_times,
        nbins=50,
        title='Distribusi Response Time API',
        labels={'x': 'Response Time (ms)', 'y': 'Frekuensi'}
    )
    fig.add_vline(x=200, line_dash="dash", line_color="red", 
                  annotation_text="Target (200 ms)")
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Throughput over time
    dates = pd.date_range(datetime.now() - timedelta(hours=24), periods=24, freq='H')
    throughput = np.random.poisson(78, 24)
    
    fig = px.line(
        x=dates, y=throughput,
        title='Throughput 24 Jam Terakhir',
        labels={'x': 'Waktu', 'y': 'Requests/detik'}
    )
    fig.update_traces(line_color='#2ECC71', line_width=2)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================
# SERVICE STATUS
# ============================================================
st.subheader("🔧 Status Microservices")

services = pd.DataFrame({
    'Service': ['Student Service', 'Achievement Service', 
                'Document Service', 'Verification Service', 'API Gateway'],
    'Status': ['🟢 Healthy', '🟢 Healthy', '🟢 Healthy', 
               '🟢 Healthy', '🟢 Healthy'],
    'Response Time (ms)': [145, 162, 178, 152, 98],
    'Requests/min': [450, 320, 210, 180, 1160],
    'Error Rate': ['0.5%', '0.8%', '1.2%', '0.6%', '0.1%']
})

st.dataframe(services, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================
# ALERTS
# ============================================================
st.subheader("🔔 System Alerts")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ All services operational")
    st.info("ℹ️ Last deployment: 2026-07-04 09:20 UTC")

with col2:
    st.warning("⚠️ Document Service response time slightly elevated")
    st.info("ℹ️ Next maintenance: 2026-07-10 02:00 UTC")

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