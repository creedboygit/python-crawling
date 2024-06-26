import requests
# import urllib3

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# response = requests.get("https://startcoding.pythonanywhere.com/basic", verify=False)
response = requests.get("https://startcoding.pythonanywhere.com/basic")
# print(response.status_code)

print(response.text)