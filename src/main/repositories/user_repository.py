from datetime import datetime, timezone
from src.main.database.mongo import db

collection = db.get_collection("users")

def create_user(user: dict):
    user["created_at"] = datetime.now(timezone.utc) 
    result = collection.insert_one(user)
    return result.inserted_id, user["created_at"]

def find_user_by_email(email: str):
    return collection.find_one({"email": email})
