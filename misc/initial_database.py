import os
import json
import firebase_admin
from firebase_admin import credentials, db

if os.getenv("GOOGLE_CREDENTIALS"):
    cred_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])
    cred = credentials.Certificate(cred_dict)
else:
    cred = credentials.Certificate("serviceAccountKey.json")
    
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://faceabsence-743dd-default-rtdb.firebaseio.com/",
    },
)
# menambahkan data dosen
ref = db.reference("Admins")

data = {
    "123456": {
        "id": "123456",
        "name": "Staff IT",
        "password": "admin",
        "email": "admin@gmail.com",
    },
}


for key, value in data.items():
    ref.child(key).set(value)
