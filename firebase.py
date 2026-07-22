import firebase_admin
from firebase_admin import credentials, firestore
import os

db = None

try:
    if not firebase_admin._apps:
        cred_path = os.getenv("FIREBASE_CREDENTIALS", "serviceAccountKey.json")
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    print("✅ Firebase Connected")

except Exception as e:
    print(f"❌ Firebase Error: {e}")