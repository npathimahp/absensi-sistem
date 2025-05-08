import os
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

with open("/app/serviceAccountKey.json") as f:
    FIREBASE_CREDENTIALS_JSON = f.read()

SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key")

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
