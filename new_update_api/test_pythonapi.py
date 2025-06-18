import requests
import json
import random

class Test_simpleBooks:

    def test_access_token(self):
        num = random.randint(1000,10000)
        url = "https://simple-books-api.glitch.me/api-clients"

        payload = json.dumps({
          "clientName": "arnu",
          "clientEmail": %f%"arnu"+"{num}+"@gmail.com"
        })
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

api = Test_simpleBooks()
api.test_access_token()