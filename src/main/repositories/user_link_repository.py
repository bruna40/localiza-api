from src.main.database.mongo import db

collection = db["user_links"]

def get_notify_user(user_id: str):
    link = collection.find_one({"user_id": user_id})
    return link["notify_user_id"] if link else None
