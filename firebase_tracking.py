
import firebase_admin
from firebase_admin import credentials, db

def init_firebase(cred_path, db_url):
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {'databaseURL': db_url})

def update_firebase_progress(user_id, module, data):
    ref = db.reference(f"/students/{user_id}/{module}")
    ref.set(data)
