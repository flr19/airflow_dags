import pytest
import requests

def test_json_response():
    #testing from mock API, where JSON response has the items in the following dict
    response = requests.get('https://gorest.co.in/public/v2/posts/')
    assert response.status_code == 200
    data = response.json()
    
    # Assert the structure of the JSON response
    assert isinstance(data, list)
    for item in data:
        assert isinstance(item, dict)
        assert 'id' in item
        assert 'user_id' in item
        assert 'title' in item
        assert 'body' in item
        # Add more assertions as needed

# Run the tests using pytest
# Run in the terminal: pytest test_api_responses_pytest.py
