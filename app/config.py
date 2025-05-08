import os
import json
from pathlib import Path
from dotenv import load_dotenv

import firebase_admin
from firebase_admin import credentials

# Load environment variables from .env file
load_dotenv()

# Ambil semua environment variable yang berkaitan dengan kredensial Firebase
firebase_credentials = {
    "type": os.getenv("FIREBASE_TYPE"),
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN")
}

# Secret key untuk Flask session
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")

# Firebase DB dan Storage
DATABASE_URL = os.getenv("DATABASE_URL")
STORAGE_BUCKET = os.getenv("STORAGE_BUCKET")

# Path ke file encode wajah (optional, sesuaikan dengan lokasi file)
ENCODE_FILE = "EncodeFile.p"

# Validasi bahwa kredensial sudah lengkap
required_keys = [
    "type", "project_id", "private_key_id", "private_key", "client_email",
    "auth_uri", "token_uri", "auth_provider_x509_cert_url", "client_x509_cert_url"
]
for key in required_keys:
    if not firebase_credentials.get(key):
        raise ValueError(f"Missing Firebase credential key: {key}")

# Inisialisasi Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_credentials)
    firebase_admin.initialize_app(cred, {
        "databaseURL": DATABASE_URL,
        "storageBucket": STORAGE_BUCKET
    })
