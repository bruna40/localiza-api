from datetime import datetime, timezone
from src.main.database.mongo import db

collection = db["user_status"]

def get_status(user_id: str):
    return collection.find_one({"user_id": user_id})

def set_entered_food_place(user_id: str, place: str):
    collection.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "status": "IN_FOOD_PLACE",
                "place": place,
                "entered_at": datetime.now(timezone.utc),
                "notified": False
            }
        },
        upsert=True
    )

def set_outside(user_id: str):
    collection.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "status": "OUTSIDE",
                "place": None,
                "entered_at": None,
                "notified": False
            }
        }
    )
