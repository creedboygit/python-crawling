import requests
from icecream import ic

header = dict()
header['X-Requested-With'] = 'XMLHttpRequest'

response = requests.get("https://startcoding.pythonanywhere.com/dynamic?page=1&keyword=", headers=header)
text = response.text
json = response.json()
ic(type(text))
ic(type(json))
# ic(text)
# ic(json)
ic(json['current_page'])
ic(json['total_pages'])

for item in json['product_data']:
    name = item['name']
    category = item['category']
    price = item['price']
    rating = item['rating']
    rating_cnt = item['rating_count']

    ic(name, category, price, rating, rating_cnt)
