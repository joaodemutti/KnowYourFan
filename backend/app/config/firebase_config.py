import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

firebase_credentials_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

if not firebase_credentials_path:
    raise ValueError("FIREBASE_CREDENTIALS_PATH not found in environment variables.")

cred = credentials.Certificate(firebase_credentials_path)

firebase_admin.initialize_app(cred)

db = firestore.client()
