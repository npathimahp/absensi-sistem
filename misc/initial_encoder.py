import os
import json
import cv2
import pickle
import face_recognition
import firebase_admin
from firebase_admin import credentials, storage
from dotenv import load_dotenv

# Load environment dari file .env
load_dotenv()

# Ambil konfigurasi dari environment
firebase_json = os.getenv("FIREBASE_CREDENTIALS_JSON")
database_url = os.getenv("DATABASE_URL")
storage_bucket = os.getenv("STORAGE_BUCKET")

# Validasi konfigurasi
if not firebase_json or not database_url or not storage_bucket:
    raise EnvironmentError("Environment variables not set properly.")

# Inisialisasi Firebase jika belum ada
if not firebase_admin._apps:
    cred_dict = json.loads(firebase_json)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(
        cred,
        {
            "databaseURL": database_url,
            "storageBucket": storage_bucket,
        },
    )

# Path ke folder gambar mahasiswa
folder_path = "./app/static/Files/Images"
if not os.path.exists(folder_path):
    raise FileNotFoundError(f"Folder not found: {folder_path}")

img_paths = os.listdir(folder_path)
img_list = []
student_ids = []

bucket = storage.bucket()

for filename in img_paths:
    full_path = os.path.join(folder_path, filename)

    if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    img = cv2.imread(full_path)
    if img is None:
        continue

    img_list.append(img)
    student_id = os.path.splitext(filename)[0]
    student_ids.append(student_id)

    # Upload ke Firebase Storage
    blob = bucket.blob(f"student_images/{filename}")
    blob.upload_from_filename(full_path)

def find_encodings(images):
    """Mencari encoding wajah dari list gambar."""
    encode_list = []
    for img in images:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img_rgb)
        if encodings:
            encode_list.append(encodings[0])
        else:
            encode_list.append(None)
    return encode_list

# Buat encoding wajah
encodings = find_encodings(img_list)
valid_data = [(e, sid) for e, sid in zip(encodings, student_ids) if e is not None]
encode_list_known, student_ids_filtered = zip(*valid_data) if valid_data else ([], [])

# Simpan ke file pickle
with open("EncodeFile.p", "wb") as file:
    pickle.dump([list(encode_list_known), list(student_ids_filtered)], file)
