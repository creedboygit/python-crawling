import requests
from bs4 import BeautifulSoup
from icecream import ic

header = dict()

header["Host"] = "widget.driverreviews.com"
header["Connection"] = "keep-alive"
header["Content-Length"] = "148"
header["sec-ch-ua"] = "\"Whale\";v=\"3\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"126\""
header["content-type"] = "application/json"
header["sec-ch-ua-mobile"] = "?0"
header["authorization"] = "742f09e77142471324bed5f1fcdb384121e070b2"
header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36"
header["sec-ch-ua-platform"] = "\"macOS\""
header["Accept"] = "*/*"
header["Origin"] = "https://www.allopneus.com"
header["Sec-Fetch-Site"] = "cross-site"
header["Sec-Fetch-Mode"] = "cors"
header["Sec-Fetch-Dest"] = "empty"
header["Referer"] = "https://www.allopneus.com/"
header["Accept-Encoding"] = "gzip, deflate, br, zstd"
header["Accept-Language"] = "ko-KR,ko;q=0.9"

data = '''
{
  "review": [
    {
      "from": 8,
      "size": 4,
      "id": "10--4855",
      "manufacturer": "Michelin",
      "model": "PRIMACY 4",
      "source": "partner",
      "vehicleType": "car",
      "lang": "fr-FR"
    }
  ]
}
'''

response = requests.post(f'https://widget.driverreviews.com/api/retailer/widget', headers=header, data=data)
html = response.text

# ic(html)

soup = BeautifulSoup(html, 'lxml')

ic(soup)