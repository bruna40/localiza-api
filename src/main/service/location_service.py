from src.main.repositories.user_link_repository import get_notify_user
from src.main.repositories.notification_repository import create_notification

def handle_user_location(user_id: str, place: str, minutes: int):
    if minutes >= 5:
        notify_user_id = get_notify_user(user_id)

        if notify_user_id:
            create_notification(
                to_user_id=notify_user_id,
                message=f"Usuário está no restaurante {place} há 5 minutos"
            )
