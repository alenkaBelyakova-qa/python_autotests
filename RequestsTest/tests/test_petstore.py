import requests
import pytest

def test_statuscode():
    response = requests.get('https://petstore.swagger.io/')
    assert response.status_code == 200

def test_name():
   response = requests.get('https://petstore.swagger.io/v2/pet/66')
   response_body = response.json()
   assert response_body['name'] == 'bublik'
