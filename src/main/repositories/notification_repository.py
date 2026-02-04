from src.main.database.mongo import db
from datetime import datetime, timezone

collection = db["notifications"]

def create_notification(
    to_user_id: str,
    from_user_id: str,
    message: str,
    type: str = "LOCATION"
):
    notification = {
        "to_user_id": to_user_id,
        "from_user_id": from_user_id,
        "type": type,
        "message": message,
        "read": False,
        "created_at": datetime.now(timezone.utc)
    }

    collection.insert_one(notification)
    return notification
