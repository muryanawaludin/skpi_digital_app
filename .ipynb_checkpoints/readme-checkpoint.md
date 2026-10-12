# 🎓 SKPI Digital - Microservices System

Aplikasi Streamlit untuk sistem SKPI Digital berbasis Microservices.

## 🚀 Demo

[Link Demo](https://skpi-digital.streamlit.app) *(jika sudah di-deploy)*

## 📋 Fitur

- 📊 **Dashboard** - Visualisasi Indikator Kinerja Utama (IKU)
- 📝 **Input Capaian** - Formulir input prestasi mahasiswa
- ✅ **Verifikasi SKPI** - Generate & verifikasi dokumen dengan QR Code
- 📈 **Monitoring System** - Real-time performance monitoring
- 👥 **Data Mahasiswa** - Database mahasiswa dengan filter

## 🏗️ Arsitektur Microservices

Aplikasi ini mensimulasikan arsitektur microservices dengan 4 layanan utama:

| Layanan | Fungsi | Teknologi |
|:--------|:-------|:----------|
| Student Service | Manajemen data mahasiswa | PostgreSQL |
| Achievement Service | Pencatatan capaian | PostgreSQL |
| Document Service | Generate SKPI + QR Code | MongoDB |
| Verification Service | Validasi dokumen | PostgreSQL |

## 🛠️ Instalasi

### Prasyarat

- Python 3.9+
- pip

### Langkah Instalasi

```bash
# 1. Clone repository
git clone https://github.com/username/skpi_digital_app.git
cd skpi_digital_app

# 2. Buat virtual environment
python -m venv venv

# 3. Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Jalankan aplikasi
streamlit run app.py