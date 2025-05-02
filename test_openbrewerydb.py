import requests
from conftest import Random_brewery
import pytest

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

def test_random():
    response1 = requests.get(f"{url}/random")
    data1 = response1.json()
    expected = data1.copy()
    
    response2 = requests.get(f"{url}/random")
    data2 = response2.json()
    
    random_field ="message"
    if random_field in expected and random_field in data2:
        assert data1[random_field] != data2[random_field], f"Field '{data2[random_field]}' should be different"

@pytest.mark.parametrize("count_per_page", [
    3,
    4,
    8
])
def test_count_breweries(count_per_page):
    response = requests.get(f"{url}?per_page={count_per_page}")
    count_breweries = response.json()
    assert len(count_breweries) == count_per_page

@pytest.mark.parametrize("expected_id", [
        "01b395ba-7b97-4214-a98c-365ad281d9dd",
        "0338af09-60df-4e16-9fd6-89d3033c9cc2",
        "084aeeb4-c3dd-4f83-9d43-732e9bac41d2"
])
def test_search_by_id(expected_id):
    response = requests.get(f"{url}/search?query=san%20diego&per_page=3")
    breweries = response.json()
    returned_ids = [brewery['id'] for brewery in breweries]
    assert expected_id in returned_ids, (
        f"Expected brewery with ID {expected_id} not found in response\n"
        f"Returned IDs: {returned_ids}"
    )