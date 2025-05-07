import os
from dotenv import load_dotenv

# Memuat variabel ENV dari file .env (opsional di Railway, tapi bagus untuk lokal)
load_dotenv()

# Path ke file yang menyimpan encoding wajah
ENCODE_FILE = "EncodeFile.p"  # Ubah jika path berbeda

# Secret key untuk Flask session
SECRET_KEY = os.getenv("SECRET_KEY")

# Firebase configuration details
FIREBASE_CREDENTIALS_JSON = os.getenv("FIREBASE_CREDENTIALS_JSON")  # Untuk Railway (JSON as string)
DATABASE_URL = os.getenv("DATABASE_URL")
STORAGE_BUCKET = os.getenv("STORAGE_BUCKET")

# Validasi environment penting
if not FIREBASE_CREDENTIALS_JSON:
    raise ValueError("FIREBASE_CREDENTIALS_JSON is not set in the environment")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the environment")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment")
if not STORAGE_BUCKET:
    raise ValueError("STORAGE_BUCKET is not set in the environment")
