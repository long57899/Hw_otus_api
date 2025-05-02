import requests
from conftest import Dog_image_response
import pytest

url = "https://dog.ceo/api/breed"

def test_list_breed_200():
    response = requests.get(f"{url}s/list/all")
    assert response.status_code == 200

def test_image_check_structure():
    response = requests.get(f"{url}s/image/random")

    data = response.json()
    try:
        validated_data = Dog_image_response(**data)
        assert validated_data.status == "success"
        assert validated_data.message.endswith(('.jpg', '.png', '.jpeg'))
    except Exception as e:
        pytest.fail(f"Validation failed: {str(e)}")

def test_random():
    response1 = requests.get(f"{url}s/image/random")
    data1 = response1.json()
    expected = data1.copy()
    
    response2 = requests.get(f"{url}s/image/random")
    data2 = response2.json()
    
    random_field ="message"
    if random_field in expected and random_field in data2:
        assert data1[random_field] != data2[random_field], f"Field '{data2[random_field]}' should be different"

@pytest.mark.parametrize("dog_images_count", [
    3,
    4,
    8
])
def test_get_breed(dog_images_count):
    response = requests.get(f"{url}/hound/images/random/{dog_images_count}")
    images = response.json()["message"]
    assert len(images) == dog_images_count

@pytest.mark.parametrize("list_sub_breeds", [
    [
        "afghan",
        "basset",
        "blood",
        "english",
        "ibizan",
        "plott",
        "walker"
    ]
])
def test_get_sub_breeds(list_sub_breeds):
    response = requests.get(f"{url}/hound/list")
    sub_breeds = response.json()["message"]
    assert sub_breeds == list_sub_breeds