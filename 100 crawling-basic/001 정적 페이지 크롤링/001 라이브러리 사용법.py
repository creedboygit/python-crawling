import requests

response = requests.get("https://startcoding.pythonanywhere.com/basic")
# print(response.status_code)

print(response.text)