import requests
import json

response = requests.get(
    "https://simple-books-api.glitch.me/books")  # getting response [response.get(url,params, headers)]
print("respose_text",response.text)  # text is used to print response
print(type(response.text))
response_json = json.loads(response.text)  # loads : used to parse json data from string
print("response json",response_json)
print(type(response_json))#


# check status code and response headers
print(response.status_code)
print(response.headers)
assert response.headers['content-type'] == 'application/json; charset=utf-8'

# reading response and writing into text file
with open('sample.txt', 'w') as file:
    for book in response_json:
        if book['type'] == 'non-fiction':
            file.write(book['name'] + '\n')
