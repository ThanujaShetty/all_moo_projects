import json
import random
from urllib.parse import urljoin
import jsonpath

import requests


class SimplebookApi:

    def access_token(self):
        global token
        with open("Authentication.json","r")as body:
            #reading file
            response = body.read()
            response_body = json.loads(response)   #converting response into json
            num = random.randint(1, 1000)
            body = {%f%"clientName":"Thanu", "clientEmail": "than"+{num}+"@gmail.com"}
            baseURL = "https://simple-books-api.glitch.me"
            resource = "/api-clients/"
            request_body=requests.post(urljoin(baseURL,resource),json=response_body)

            #to fetch accessToken
            res = json.loads(request_body.text)
            token=jsonpath.jsonpath(res,"accessToken")
            print(token)

    def create_book(self):
        global orderId
        with open("create_book.json","r")as body:
            request = body.read()
            request_body = json.loads(request)
            baseUrl = "https://simple-books-api.glitch.me"
            resource = "/orders"
            headers = {'Authorization':'Bearer '+ token[0]}
            response_body = requests.post(urljoin(baseUrl,resource),json=request_body,headers=headers)
            print(response_body)

            # to fetch orderId
            res = json.loads(response_body.text)
            orderId = jsonpath.jsonpath(res, "orderId")
            print(orderId)

    def get_an_order_api(self):
        baseUrl = "https://simple-books-api.glitch.me"
        resource = "/orders/"+ str(orderId[0])
        headers = {"Authorization": 'Bearer '+ token[0]}
        response_body = requests.get(urljoin(baseUrl,resource),headers=headers)
        print("get_order_api ",response_body)

        #get orders details
        res = json.loads(response_body.text)
        print(res)

    def update_an_order(self):
        with open("update_order.json")as body:
            response =body.read()
            response_body =json.loads(response)
            baseURL = "https://simple-books-api.glitch.me"
            resource = "/orders/"+str(orderId[0])
            headers = {"Authorization": 'Bearer ' + token[0] }
            requests_body = requests.patch(urljoin(baseURL,resource,),json=response_body,headers=headers)
            print("update ",requests_body)

    def delete_book(self):
        baseURL = "https://simple-books-api.glitch.me"
        resource = "/orders/"+str(orderId[0])
        headers = {"Authorization": 'Bearer ' + token[0] }
        requests_body = requests.patch(urljoin(baseURL, resource), headers=headers)
        print("delete api",requests_body)

api = SimplebookApi()
api.access_token()
api.create_book()
api.get_an_order_api()
api.update_an_order()
api.delete_book()

