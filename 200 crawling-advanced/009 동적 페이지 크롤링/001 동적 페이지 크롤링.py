import requests
import urllib3
from icecream import ic

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

header = dict()
header["Host"] = "startcoding.pythonanywhere.com"
# header["Connection"] = "keep-alive"
header["Accept"] = "application/json, text/javascript, */*; q=0.01"
header["Referer"] = "https://startcoding.pythonanywhere.com/dynamic"
header["Accept-Language"] = "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
header["Content-Type"] = "application/json"
header["Connection"] = "keep-alive"
header["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Whale/3.26.244.21 Safari/537.36"
header["X-Requested-With"] = "XMLHttpRequest"

response = requests.get("https://startcoding.pythonanywhere.com/dynamic?page=1&keyword=", headers=header, verify=False)
json_response = response.json()
ic(json_response)
