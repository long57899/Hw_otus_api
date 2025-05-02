import requests
from conftest import Placeholder_post
import pytest

url = "https://jsonplaceholder.typicode.com/"

def test_responce_200():
    response = requests.get(f"{url}todos")
    assert response.status_code == 200

@pytest.mark.parametrize("count_posts",[
    100
    ])

def test_posts(count_posts):
    response = requests.get(f"{url}posts")
    data = response.json()
    assert len(data) == count_posts , f"The number of posts in the response{len(data)} but should be {count_posts}"

def test_check_post_structure():
    response = requests.get(f"{url}todos/1")

    data = response.json()
    try:
        validated_data = Placeholder_post(**data)
        assert validated_data.userId == 1
        assert validated_data.id == 1
        assert validated_data.title == "delectus aut autem"
        assert validated_data.completed == False # noqa

    except Exception as e:
        pytest.fail(f"Validation failed: {str(e)}")

@pytest.mark.parametrize("c_count_posts, w_count_posts", [
    (5, 2)
])
def test_count_posts_positive_and_negative(c_count_posts , w_count_posts):
    response = requests.get(f"{url}/posts/1/comments")
    response_count = response.json()
    assert len(response_count) == c_count_posts, f"The correct number of posts is {c_count_posts}, but the response has {len(response_count)}"
    assert len(response_count) != w_count_posts, f"The number of posts in the response cannot be {c_count_posts}"

@pytest.mark.parametrize("post_id", [
        1,
        2,
        3
])
def test_check_post_link_id(post_id):
    response = requests.get(f"{url}//posts/{post_id}")
    responce_post = response.json()
    assert responce_post["id"] == post_id , "The received field POST does not match the one sent. "
    