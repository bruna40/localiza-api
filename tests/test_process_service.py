import pytest
from src.main.service import process_service
from src.main.models.location_dto import LocationDTO


@pytest.mark.parametrize(
    "latitude, longitude, expected_status",
    [
        (-21.7834440, -43.3357114, "IN_FOOD_PLACE"),  
        (-3.7319051, -38.4909180, "IN_FOOD_PLACE"),  
        (0, 0, "OUTSIDE"),                          
        (51.5074, -0.1278, "OUTSIDE"),                
    ]
)
def test_location_multiple_coordinates(monkeypatch, latitude, longitude, expected_status):

    def fake_check_place(lat, lon):
        if expected_status == "IN_FOOD_PLACE":
            return {
                "is_food": True,
                "name": "Mock Restaurant",
                "type": "restaurant"
            }
        return {"is_food": False}

    monkeypatch.setattr(
        process_service,
        "check_place_osm",
        fake_check_place
    )

    data = LocationDTO(
        user_id="1",
        latitude=latitude,
        longitude=longitude
    )

    result = process_service.process_location(data)

    assert result["status"] == expected_status
