import requests
from pydantic import BaseModel, Field
from typing import Optional
import pytest



class Random_brewery(BaseModel):
    id: str
    name: str
    brewery_type: Optional[str] = Field(None)
    address_1: Optional[str] = Field(None)
    address_2: Optional[str] = Field(None)
    address_3: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    state_province: Optional[str] = Field(None)
    postal_code: Optional[str] = Field(None)
    country: Optional[str] = Field(None)
    longitude: Optional[float] = Field(None)
    latitude: Optional[float] = Field(None)
    phone: Optional[str] = Field(None)
    website_url: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    street: Optional[str] = Field(None)




url = "https://api.openbrewerydb.org/v1/breweries"

def test_responce_200():
    response = requests.get(f"{url}/random")
    assert response.status_code == 200

def test_random_brewery_check_structure():
    response = requests.get(f"{url}/random")

    data = response.json()
    
    try:
        Random_brewery(**data[0])

    except Exception as e:
        pytest.fail(f"Validation failed: {str(e)}")

