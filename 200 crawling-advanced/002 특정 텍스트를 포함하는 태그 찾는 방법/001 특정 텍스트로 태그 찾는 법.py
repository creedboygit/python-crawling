import requests
from bs4 import BeautifulSoup

response = requests.get("https://startcoding.pythonanywhere.com/basic")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

'''
텍스트와 똑같은 태그 하나 찾기
'''
find = soup.find('p', string='노트북')
print(find)

'''
텍스트와 똑같은 태그 여러개 찾기
'''
find = soup.find_all('p', string='노트북')
print(find)