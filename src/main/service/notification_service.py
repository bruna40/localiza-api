from src.main.repositories.notification_repository import create_notification

def notify_user_location(
    to_user_id: str,
    from_user_id: str,
    place: str
):
    message = f"Usuário está no restaurante {place} há 5 minutos"

    return create_notification(
        to_user_id=to_user_id,
        from_user_id=from_user_id,
        message=message
    )
