import requests as rq

URL = "http://127.0.0.1:1234"

json_data = {"data": "this is a test"}

rq.post(f"{URL}/post", json=json_data)

get = rq.get(f"{URL}/get")
print(get.json())