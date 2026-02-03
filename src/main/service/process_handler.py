import requests

FOOD_TYPES = {"restaurant", "cafe", "fast_food", "bar"}

def check_place_osm(lat: float, lon: float):
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": "restaurant",
        "format": "json",
        "limit": 1,
        "viewbox": f"{lon-0.001},{lat-0.001},{lon+0.001},{lat+0.001}",
        "bounded": 1
    }

    headers = {
        "User-Agent": "location-portfolio-app"
    }

    response = requests.get(url, params=params, headers=headers, timeout=5)
    data = response.json()

    if not data:
        return {"is_food": False}

    place = data[0]

    is_food = (
        place.get("class") == "amenity"
        and place.get("type") in FOOD_TYPES
    )

    return {
        "is_food": is_food,
        "name": place.get("display_name"),
        "type": place.get("type")
    }
