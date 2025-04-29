import firebase_admin
from firebase_admin import credentials, firestore, storage
import os
from dotenv import load_dotenv

load_dotenv()

firebase_credentials_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
firebase_bucket = os.getenv("FIREBASE_STORAGE_BUCKET")

if not firebase_credentials_path:
    raise ValueError("FIREBASE_CREDENTIALS_PATH not found in environment variables.")

if not firebase_bucket:
    raise ValueError("FIREBASE_STORAGE_BUCKET not found in environment variables.")

cred = credentials.Certificate(firebase_credentials_path)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'storageBucket': firebase_bucket
    })

db = firestore.client()
bucket = storage.bucket()
