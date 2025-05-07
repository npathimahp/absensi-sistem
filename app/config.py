import os
from dotenv import load_dotenv

# Memuat variabel ENV dari file .env
load_dotenv()

# Path ke file yang menyimpan encoding wajah
ENCODE_FILE = "EncodeFile.p"  # Atau sesuaikan dengan path yang benar

# Secret key untuk Flask session
SECRET_KEY = "your_secret_key_here"

# Firebase configuration details
FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")  # Mengambil dari ENV
DATABASE_URL = os.getenv("DATABASE_URL")
STORAGE_BUCKET = os.getenv("STORAGE_BUCKET")

# Opsional: Cek jika variabel ENV tidak ditemukan
if not FIREBASE_CREDENTIALS:
    raise ValueError("FIREBASE_CREDENTIALS is not set in the environment")
