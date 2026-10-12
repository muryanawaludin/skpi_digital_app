"""
Konfigurasi aplikasi SKPI Digital
"""

APP_TITLE = "SKPI Digital - Microservices System"
APP_ICON = "🎓"
UNIVERSITY = "Universitas Dirgantara Marsekal Suryadarma"
FACULTY = "Fakultas Ilmu Komputer dan Desain (FIKD)"

# Warna tema
COLORS = {
    "primary": "#3498DB",
    "success": "#2ECC71",
    "warning": "#E67E22",
    "danger": "#E74C3C",
    "info": "#9B59B6",
    "neutral": "#95A5A6"
}

# Indikator kinerja utama
KPI_DATA = {
    "Indikator": [
        "Waktu Proses SKPI",
        "Test Coverage",
        "UAT Satisfaction",
        "Error Rate Data",
        "API Response Time",
        "Throughput",
        "User Satisfaction"
    ],
    "Target": [">70%", ">90%", ">85%", "<1%", "<200 ms", "50 req/s", "≥4.2"],
    "Hasil": ["↓73.1%", "92.3%", "87.5%", "0.8%", "156 ms", "78 req/s", "4.3"],
    "Status": ["✅ Melebihi", "✅ Tercapai", "✅ Tercapai", 
               "✅ Tercapai", "✅ Tercapai", "✅ Melebihi", "✅ Tercapai"]
}