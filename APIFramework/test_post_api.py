import requests
import json
from add_book import *

# Generate access token
response = requests.post('https://simple-books-api.glitch.me//api-clients/',
                         json={"clientName": "Hitha8989nk", "clientEmail": "Hithatn78787@example.com"})
token = json.loads(response.text)
access_token = token['accessToken']

headers = {
    'Authorization': 'Bearer ' + access_token}

# Add book using post API
# response1 = requests.post('https://simple-books-api.glitch.me/orders',
#                           json={"bookId": 1, "customerName": "Roby"}, headers=headers)
#
# response_book = response1.json()
# print(response_book)

# adding book details dynamically
response1 = requests.post('https://simple-books-api.glitch.me/orders',
                          json=add_book_details('reenu'), headers=headers)

response_book = response1.json()
print(response_book)
