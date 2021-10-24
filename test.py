import requests

token = "OGJhYmVhMjMtOGI0Mi00MDVhLTkwZDktZDZjZGRlMzUxMTlk"
api_auth = {'Authorization' : f'Bearer {token}'}

json_data_c = {"record": {"email": "noel@gmail.com", "id": "420", "password": "noelnoel", "username": "noel"}, "table": "Users"}
json_data_b = {"table": "users"}

c = requests.post("https://api.m3o.com/v1/db/Create", headers=api_auth, json=json_data_c)
b = requests.get("https://api.m3o.com/v1/db/Count", headers=api_auth, json=json_data_b)

json_c = c.json()
json_b = b.json()

print(f"JSON response creation: {json_c}")
print(f"JSON response count: {json_b}")
#47397600