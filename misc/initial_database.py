import os
import json
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

# Load environment (penting saat lokal, diabaikan Railway)
load_dotenv()

# Pastikan semua variabel tersedia
firebase_json = os.getenv("FIREBASE_CREDENTIALS_JSON")
database_url = os.getenv("DATABASE_URL")

if not firebase_json or not database_url:
    raise EnvironmentError("FIREBASE_CREDENTIALS_JSON or DATABASE_URL is not set.")

# Inisialisasi Firebase (hindari duplikat)
if not firebase_admin._apps:
    cred_dict = json.loads(firebase_json)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(
        cred,
        {
            "databaseURL": "https://faceabsence-743dd-default-rtdb.firebaseio.com/",
        },
    )

# Menambahkan data admin ke database
ref = db.reference("Admins")

data = {
    "123456": {
        "id": "123456",
        "name": "Staff IT",
        "password": "admin",  # NOTE: gunakan hash untuk produksi
        "email": "admin@gmail.com",
    },
}

for key, value in data.items():
    ref.child(key).set(value)
