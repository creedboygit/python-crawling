import requests
import trafilatura
import json
from datetime import datetime


def extract_and_convert_to_json(url):
    # URL에서 콘텐츠 다운로드
    downloaded = trafilatura.fetch_url(url)

    # 텍스트 추출
    text = trafilatura.extract(downloaded)

    # 메타데이터 추출
    metadata = trafilatura.extract(downloaded, output_format='metadata')

    # 결과를 딕셔너리로 구조화
    result = {
        "url": url,
        "extracted_text": text,
        # "title": metadata.get('title', ''),
        # "author": metadata.get('author', ''),
        # "date": metadata.get('date', ''),
        # "hostname": metadata.get('hostname', ''),
        # "description": metadata.get('description', ''),
        # "categories": metadata.get('categories', []),
        # "tags": metadata.get('tags', []),
        "extraction_date": datetime.now().isoformat()
    }

    # 딕셔너리를 JSON 문자열로 변환
    json_result = json.dumps(result, ensure_ascii=False, indent=2)

    return json_result


# 사용 예
url = "https://kin.naver.com/search/list.naver?query=이어폰"
json_output = extract_and_convert_to_json(url)
print(json_output)

# JSON을 파일로 저장하고 싶다면:
# with open('output.json', 'w', encoding='utf-8') as f:
#     f.write(json_output)
