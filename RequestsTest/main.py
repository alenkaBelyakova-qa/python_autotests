import requests 

# Создание питомца
response = requests.get("https://petstore.swagger.io/v2/pet", json={
  "id": 66,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "bublik",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

# Смена имени питомца
response = requests.put("https://petstore.swagger.io/v2/pet",json={
  "id": 66,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "bublik",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

# Нахождение пет по ID
response = requests.get("https://petstore.swagger.io/v2/pet/66")
print(response.text)