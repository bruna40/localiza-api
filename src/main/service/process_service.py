from src.main.service.process_handler import check_place_osm

def process_location(data):
    result = check_place_osm(
        data.latitude,
        data.longitude
    )

    if result.get("is_food"):
        return {
            "status": "IN_FOOD_PLACE",
            "place": result.get("name"),
            "type": result.get("type")
        }

    return {
        "status": "OUTSIDE",
        "type": result.get("type")
    }
