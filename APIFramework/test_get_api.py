import requests
import json

response = requests.get('https://simple-books-api.glitch.me/books')
# res = json.loads(response.text)
json_resp = response.json()  # internally calls loads() to parse response to python obj
print(json_resp)

#get type of book from the
assert response.status_code == 200 # to check status code

if response.headers['content-type'] == 'application/json; charset=utf-8':
    for book in json_resp:
        if book['type'] == 'fiction':
            print(book['name'])