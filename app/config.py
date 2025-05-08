import os
import json
from dotenv import load_dotenv

# Memuat variabel dari file .env (penting untuk lokal dev)
load_dotenv()

# Path ke file encoding wajah
ENCODE_FILE = "EncodeFile.p"  # Sesuaikan jika berbeda

# Secret key untuk Flask
SECRET_KEY = os.getenv("SECRET_KEY")

# Firebase config dari string JSON
FIREBASE_CREDENTIALS_JSON = os.getenv("FIREBASE_CREDENTIALS_JSON")
if FIREBASE_CREDENTIALS_JSON:
    try:
        FIREBASE_CREDENTIALS = json.loads(FIREBASE_CREDENTIALS_JSON)
    except json.JSONDecodeError:
        raise ValueError("FIREBASE_CREDENTIALS_JSON is not a valid JSON")
else:
    raise ValueError("FIREBASE_CREDENTIALS_JSON is not set in environment")

# Firestore database URL & storage bucket
DATABASE_URL = os.getenv("DATABASE_URL")
STORAGE_BUCKET = os.getenv("STORAGE_BUCKET")

# Validasi variabel penting lainnya
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in environment")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment")
if not STORAGE_BUCKET:
    raise ValueError("STORAGE_BUCKET is not set in environment")
