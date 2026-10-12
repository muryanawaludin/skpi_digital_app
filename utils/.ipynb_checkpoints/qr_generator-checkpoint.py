"""
Generator QR Code untuk verifikasi SKPI
"""

import qrcode
from PIL import Image
import io

def generate_qr_code(data, size=200):
    """
    Generate QR Code dari data string
    
    Args:
        data (str): Data yang akan di-encode
        size (int): Ukuran QR code dalam pixel
    
    Returns:
        PIL.Image: Gambar QR Code
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((size, size), Image.LANCZOS)
    return img

def qr_to_bytes(img):
    """Konversi PIL Image ke bytes untuk download"""
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return buf.getvalue()