import pytest
import requests

@pytest.mark.parametrize("api_endpoint", [
    "https://gorest.co.in/public/v2/posts/",  # Modify this with your actual API endpoint
])
def test_json_response(api_endpoint):
    response = requests.get(api_endpoint)
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)
    for item in data:
        assert isinstance(item, dict)
        assert 'id' in item
        assert 'user_id' in item
        assert 'title' in item
        assert 'body' in item
        # Add more assertions as needed
