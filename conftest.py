from pydantic import BaseModel, Field
from typing import Optional

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

class Dog_image_response(BaseModel):
    message: str
    status: str

class Placeholder_post(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool

def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru",action="store", help="Please provide a link.")
    parser.addoption("--status_code", default=200 ,action="store", type=int, help="Please provide a status code.")