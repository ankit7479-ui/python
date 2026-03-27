import requests

#GET
response = requests.get("http://api.github.com/user")
print(response.status_code)
print(response.json())

#POST
data = {"name": "Alice", "age": 25}
response = requests.get("http://api.github.com/user",json=data)
print(response.status_code)

