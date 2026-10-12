"""
Simulasi database in-memory untuk microservices
"""

import pandas as pd
from datetime import datetime

class Database:
    """Simulasi database untuk aplikasi SKPI Digital"""
    
    def __init__(self):
        self.students = self._init_students()
        self.achievements = self._init_achievements()
        self.documents = self._init_documents()
        self.verifications = self._init_verifications()
    
    def _init_students(self):
        """Inisialisasi data mahasiswa"""
        return pd.DataFrame({
            'NIM': ['241051007', '231051001', '241051002', '231051003', '251051001'],
            'NAMA': ['Nazmatul Muizzah', 'Avrinka Putra', 'Sherly Saskia', 
                     'Lina Puspitasari', 'Isnanda Ramadhan'],
            'PRODI': ['Sistem Informasi', 'Sistem Informasi', 'Sistem Informasi',
                      'Sistem Informasi', 'Sistem Informasi'],
            'ANGKATAN': ['2024', '2023', '2024', '2023', '2025'],
            'JALUR': ['Reguler Pagi', 'Reguler Pagi', 'Reguler Pagi',
                      'Reguler Pagi', 'Reguler Pagi']
        })
    
    def _init_achievements(self):
        """Inisialisasi data capaian"""
        return pd.DataFrame(columns=[
            'ID', 'NIM', 'JENIS', 'NAMA_KEGIATAN', 'TINGKAT', 
            'TANGGAL', 'STATUS', 'VALIDATOR'
        ])
    
    def _init_documents(self):
        """Inisialisasi data dokumen SKPI"""
        return pd.DataFrame(columns=[
            'ID_DOKUMEN', 'NIM', 'TANGGAL_TERBIT', 'QR_CODE', 'STATUS'
        ])
    
    def _init_verifications(self):
        """Inisialisasi data verifikasi"""
        return pd.DataFrame(columns=[
            'ID_VERIFIKASI', 'ID_DOKUMEN', 'VERIFIKATOR', 'TANGGAL', 'STATUS'
        ])
    
    # ============ STUDENT SERVICE ============
    def get_student(self, nim):
        """Ambil data mahasiswa berdasarkan NIM"""
        result = self.students[self.students['NIM'] == nim]
        return result.iloc[0].to_dict() if not result.empty else None
    
    def get_all_students(self):
        """Ambil semua data mahasiswa"""
        return self.students
    
    # ============ ACHIEVEMENT SERVICE ============
    def add_achievement(self, nim, jenis, nama_kegiatan, tingkat, tanggal):
        """Tambah capaian baru"""
        new_id = len(self.achievements) + 1
        new_data = pd.DataFrame([{
            'ID': f'ACH{new_id:04d}',
            'NIM': nim,
            'JENIS': jenis,
            'NAMA_KEGIATAN': nama_kegiatan,
            'TINGKAT': tingkat,
            'TANGGAL': tanggal,
            'STATUS': 'Pending',
            'VALIDATOR': None
        }])
        self.achievements = pd.concat([self.achievements, new_data], ignore_index=True)
        return new_data.iloc[0].to_dict()
    
    def get_achievements(self, nim=None):
        """Ambil capaian (semua atau berdasarkan NIM)"""
        if nim:
            return self.achievements[self.achievements['NIM'] == nim]
        return self.achievements
    
    def validate_achievement(self, achievement_id, validator, status):
        """Validasi capaian"""
        mask = self.achievements['ID'] == achievement_id
        self.achievements.loc[mask, 'STATUS'] = status
        self.achievements.loc[mask, 'VALIDATOR'] = validator
        return True
    
    # ============ DOCUMENT SERVICE ============
    def generate_document(self, nim):
        """Generate dokumen SKPI"""
        new_id = f'SKPI{len(self.documents)+1:04d}'
        new_data = pd.DataFrame([{
            'ID_DOKUMEN': new_id,
            'NIM': nim,
            'TANGGAL_TERBIT': datetime.now().strftime('%Y-%m-%d'),
            'QR_CODE': f'https://skpi.unsurya.ac.id/verify/{new_id}',
            'STATUS': 'Generated'
        }])
        self.documents = pd.concat([self.documents, new_data], ignore_index=True)
        return new_data.iloc[0].to_dict()
    
    def get_documents(self, nim=None):
        """Ambil dokumen"""
        if nim:
            return self.documents[self.documents['NIM'] == nim]
        return self.documents
    
    # ============ VERIFICATION SERVICE ============
    def verify_document(self, document_id):
        """Verifikasi dokumen"""
        doc = self.documents[self.documents['ID_DOKUMEN'] == document_id]
        if doc.empty:
            return {'valid': False, 'message': 'Dokumen tidak ditemukan'}
        
        # Cek capaian yang sudah divalidasi
        nim = doc.iloc[0]['NIM']
        achievements = self.get_achievements(nim)
        validated = achievements[achievements['STATUS'] == 'Approved']
        
        return {
            'valid': True,
            'document': doc.iloc[0].to_dict(),
            'student': self.get_student(nim),
            'achievements': validated.to_dict('records'),
            'total_achievements': len(validated)
        }

# Inisialisasi database global
db = Database()