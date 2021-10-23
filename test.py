import random
import requests

token = "OGJhYmVhMjMtOGI0Mi00MDVhLTkwZDktZDZjZGRlMzUxMTlk"
api_auth = {'Authorization' : f'Bearer {token}'}

user_id = str(random.randint(10000000,99999999))
user_register_data = {"email": "nosel@gmail.com", "id": user_id, "password": "leonleon", "username": "nosel"}

b = requests.post("https://api.m3o.com/v1/user/Create", headers=api_auth, data=user_register_data)
#b = requests.post("https://api.m3o.com/v1/user/Create", headers=api_auth, data='{"email": "nosel@gmail.com", "id": user_id, "password": "leonleon", "username": "nosel"}')