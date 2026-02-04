from datetime import datetime, timezone
from src.main.database.mongo import db
from bson import ObjectId

collection = db.get_collection("users")

def create_user(user: dict):
    user["created_at"] = datetime.now(timezone.utc) 
    result = collection.insert_one(user)
    return result.inserted_id, user["created_at"]

def find_user_by_email(email: str):
    return collection.find_one({"email": email})

def find_by_user_id(user_id: str):
    return collection.find_one({
        "_id": ObjectId(user_id),
        "deleted_at": None
    })




def update_user_name(user_id: str, name: str):
    user = collection.find_one_and_update(
        {"_id": ObjectId(user_id)},
        {
            "$set": {
                "name": name,
                "updated_at": datetime.now(timezone.utc)
            }
        },
        return_document=True
    )

    if not user:
        return None

    user["id"] = str(user["_id"])
    del user["_id"]

    return user


def soft_delete_user(user_id: str):
    collection.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$set": {
                "deleted_at": datetime.now(timezone.utc)
            }
        }
    )