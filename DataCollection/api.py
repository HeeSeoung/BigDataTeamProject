import requests
import json

headers = {
    'Content-Type': 'application/json'
}

data = {
    'login-code': "123456",
    'phone': '+821086094104'
}

rsp = requests.post('https://web-production.lime.bike/api/rider/v1/login', headers=headers, data=data)
