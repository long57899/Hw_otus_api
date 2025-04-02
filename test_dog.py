import requests
from pydantic import BaseModel
from typing import List
import pytest



class Dog_image_response(BaseModel):
    message: str
    status: str




url = "https://dog.ceo/api/breeds"

def test_list_breed():
    response = requests.get(f"{url}/list/all")
    assert response.status_code == 200

def test_image():
    response = requests.get(f"{url}/image/random")

    data = response.json()
    try:
        validated_data = Dog_image_response(**data)
        assert validated_data.status == "success"
        assert validated_data.message.endswith(('.jpg', '.png', '.jpeg'))
    except Exception as e:
        pytest.fail(f"Validation failed: {str(e)}")