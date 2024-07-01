''' 상세 페이지 요청 함수 '''
import requests
from bs4 import BeautifulSoup


def get_detail(link):
    # 헤더 추가
    header = {
        "referer": link.encode('utf-8')
    }

    detail_response = requests.get(link, headers=header)
    detail_html = detail_response.text
    detail_soup = BeautifulSoup(detail_html, 'html.parser')

    return detail_soup