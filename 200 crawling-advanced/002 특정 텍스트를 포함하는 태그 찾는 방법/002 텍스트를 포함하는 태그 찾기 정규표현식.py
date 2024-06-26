import requests
import re
from bs4 import BeautifulSoup

response = requests.get("https://startcoding.pythonanywhere.com/basic")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

'''
텍스트를 포함하는 태그 하나 찾기
soup.find('태그명', string=re.compile('텍스트'))

텍스트를 포함하는 태그 하나 찾기 (정규표현식)
- re는 regular expression의 약자
- compile은 패턴을 해석함
- soup.find('태그명', string=re.compile('텍스트'))
'''
find = soup.find('p', string='노트북')
print(find)

'''
텍스트를 포함하는 태그 여러개 찾기 (정규표현식)
- soup.find_all('태그명', string=re.compile('텍스트'))
'''
find = soup.find_all('p', string='노트북')
print(find)

'''
텍스트로 시작하는 태그 한개 찾기 (정규표현식)
- soup.find('태그명', string=re.complie('^텍스트'))
'''
print("===========")
find = soup.find('a', string=re.compile('^레노버'))
print(find)

'''
텍스트로 시작하는 태그 여러개 찾기 (정규표현식)
- soup.find('태그명', string=re.complie('^텍스트'))
'''
print("===========")
find = soup.find_all('a', string=re.compile('^레노버'))
print(find)

'''
텍스트로 끝나는 태그 한개 찾기 (정규표현식)
- soup.find('태그명', string=re.complie('텍스트$'))
'''
find = soup.find('a', string=re.compile('KR$'))
print("===========")
print(find)

'''
텍스트로 끝나는 태그 여러개 찾기 (정규표현식)
- soup.find('태그명', string=re.complie('텍스트$'))
'''
find = soup.find_all('a', string=re.compile('KR$'))
print("===========")
print(find)

