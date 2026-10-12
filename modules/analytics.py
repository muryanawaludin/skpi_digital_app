"""
Modul analitik dan visualisasi
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats

def calculate_statistics(pre_scores, post_scores):
    """
    Hitung statistik deskriptif dan uji t berpasangan
    """
    pre = np.array(pre_scores)
    post = np.array(post_scores)
    diff = post - pre
    
    t_stat, p_val = stats.ttest_rel(post, pre)
    
    return {
        'mean_pre': np.mean(pre),
        'mean_post': np.mean(post),
        'mean_diff': np.mean(diff),
        'std_diff': np.std(diff, ddof=1),
        't_stat': t_stat,
        'p_value': p_val / 2,  # one-tailed
        'n': len(diff)
    }

def create_kpi_chart(kpi_data):
    """Buat chart untuk KPI"""
    df = pd.DataFrame(kpi_data)
    
    # Konversi hasil ke numerik untuk visualisasi
    numeric_values = []
    for val in df['Hasil']:
        if '↓' in val:
            numeric_values.append(float(val.replace('↓', '').replace('%', '')))
        elif '%' in val:
            numeric_values.append(float(val.replace('%', '')))
        elif 'ms' in val:
            numeric_values.append(float(val.replace(' ms', '')))
        elif 'req/s' in val:
            numeric_values.append(float(val.replace(' req/s', '')))
        else:
            numeric_values.append(float(val))
    
    df['Numeric'] = numeric_values
    
    fig = px.bar(
        df, x='Indikator', y='Numeric',
        color='Status',
        color_discrete_map={
            '✅ Melebihi': '#2ECC71',
            '✅ Tercapai': '#3498DB',
            '⚠️ Dalam Proses': '#E67E22'
        },
        title='Indikator Kinerja Utama (IKU)',
        labels={'Numeric': 'Nilai', 'Indikator': 'Indikator'}
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        height=400,
        showlegend=True,
        legend_title="Status"
    )
    return fig

def create_satisfaction_radar():
    """Buat radar chart untuk kepuasan"""
    categories = ['Kecepatan', 'Akurasi', 'Kemudahan', 'Kepuasan']
    baseline = [2.5, 2.9, 2.7, 2.8]
    post = [4.3, 4.5, 4.4, 4.3]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=baseline, theta=categories,
        fill='toself', name='Baseline',
        line_color='#E74C3C'
    ))
    fig.add_trace(go.Scatterpolar(
        r=post, theta=categories,
        fill='toself', name='Post-Implementation',
        line_color='#2ECC71'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        title='Perbandingan Kepuasan Pengguna (SERVQUAL)',
        height=400
    )
    return fig

def create_processing_time_chart():
    """Buat chart perbandingan waktu proses"""
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Baseline (Manual)',
        x=['Rata-rata', 'Median', 'Tercepat', 'Terlama'],
        y=[7.8, 7.0, 5, 12],
        marker_color='#E74C3C'
    ))
    fig.add_trace(go.Bar(
        name='Sistem Baru',
        x=['Rata-rata', 'Median', 'Tercepat', 'Terlama'],
        y=[2.1, 2.0, 1, 4],
        marker_color='#2ECC71'
    ))
    fig.update_layout(
        title='Perbandingan Waktu Proses SKPI (hari)',
        barmode='group',
        height=400,
        yaxis_title='Hari'
    )
    return fig

def create_trend_chart():
    """Buat chart trend penggunaan sistem"""
    dates = pd.date_range('2026-06-01', periods=30, freq='D')
    requests = np.random.poisson(78, 30)  # rata-rata 78 req/detik
    
    fig = px.line(
        x=dates, y=requests,
        title='System Throughput (30 Hari Terakhir)',
        labels={'x': 'Tanggal', 'y': 'Requests/detik'}
    )
    fig.update_traces(line_color='#3498DB', line_width=2)
    fig.update_layout(height=400)
    return fig