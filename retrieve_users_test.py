import pytest
import requests

"""
Tests the save_users_from_webservice.py DAG

Checks for the attributes and that list size is 4

Author:
    Farah Lubaba Rouf

"""

def test_json_response():
    #testing from mock API, where JSON response has the items in the following dict
    response = requests.get('https://api.mocki.io/v2/11fe220e/users')
    assert response.status_code == 200
    data = response.json()
    
    # Assert the structure of the JSON response
    assert isinstance(data, list)
    for item in data:
        assert isinstance(item, dict)
        assert 'id' in item
        assert 'name' in item
        assert 'email' in item
        assert 'age' in item
        # Add more assertions as needed
    
    # Assertlist size == 4

def test_size():
    response = requests.get('https://api.mocki.io/v2/11fe220e/users')
    data = response.json()
    assert len(data) == 4

# Run the tests using pytest
# Run in the terminal: pytest test_api_responses_pytest.py
