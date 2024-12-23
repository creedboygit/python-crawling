import streamlit as st
import requests
import pandas as pd

# Streamlit page setup
st.set_page_config(page_title="Real Estate Listings Viewer", layout="wide")
st.title("Real Estate Listings from Pages 1 to 10")
st.markdown("This page fetches and displays real estate listings from pages 1 to 10 using the Naver Real Estate API.")

# Define the cookies and headers as provided
cookies = {
    'NSCS': '1',
    'ASID': 'de6d3fad0000018bfc266dd600000045',
    '_ga_1THKVZ9Q8W': 'GS1.1.1701436392.2.0.1701436392.60.0.0',
    '_fwb': '167zEj593YWD8Oauc7eODSo.1702433942332',
    '_tt_enable_cookie': '1',
    '_ttp': 'S2T9izlEqdWxCxZjwxzhGvEh1_m',
    '_ga_4BKHBFKFK0': 'GS1.1.1705152462.1.1.1705152467.55.0.0',
    '_fwb': '186lnNd66PWfMIvZbL8TEbj.1708260296889',
    'NNB': 'PO5L5IZFRDQWK',
    'NFS': '2',
    'm_loc': '8ff896e91706fbc1adddcab7477a096fcee741096725b1e6c8d8658cc217a7b6a09e33d6988982b14dbf50ce9098692a',
    '_ga_EFBDNNF91G': 'GS1.1.1720251571.1.0.1720251577.0.0.0',
    'tooltipDisplayed': 'true',
    'NID_AUT': 'TcWpgbnbVkHD9g0UpNjuaabFaqHBmUZHPv5VE15AZ4LbJ0fRrB9yu8bcaRoy5/qe',
    'NID_JKL': 'YcZdBhtCO7Jb799V9+lWMCRcpFX5KUXPIcLvRLUg5NM=',
    'recent_card_list': '10226',
    'BNB_FINANCE_HOME_TOOLTIP_MYASSET': 'true',
    'wcs_bt': '4f99b5681ce60:1733033164',
    '_fbp': 'fb.1.1733047589437.621516362542158689',
    '_ga_451MFZ9CFM': 'GS1.1.1733054846.2.1.1733054868.0.0.0',
    '_fbc': 'fb.1.1733400349477.PAZXh0bgNhZW0CMTEAAaaOhgY-O2C8KNMdIXXqvg6aLgz-WbRpldObuvuGT_nmHWRTDd0vEYyDScA_aem_ikeqAQKr5-_AIDJqJcBIOA',
    '_ga': 'GA1.2.1213673474.1701432613',
    '_ga_6Z6DP60WFK': 'GS1.2.1734093180.3.0.1734093180.60.0.0',
    'NAC': '1IyjBQAPbIAO',
    'NV_WETR_LAST_ACCESS_RGN_M': '"MDkxNDA2MzU="',
    'NV_WETR_LOCATION_RGN_M': '"MDkxNDA2MzU="',
    'NACT': '1',
    'SRT30': '1734944705',
    'NID_SES': 'AAAB2Is8JNlbUbZ9296Dh6mQqsQO3FW1Bno6RUSJqUevhqGTHnAnsA4C4XLumwmWz9MFkMpkav2XBXrjEy0+zc82EJOnV1IVEOtPxaYHE/q26HfGH7YwT+7kRYFXHwiN9810P08+FRJdXuzWZRyyrSk/W9DVOa9IvreZqFdOuBc85oR2fmfCBQdd/xBcdYYm/5QNKudMKKa8ZKnKeDwLBT0TlRL5HhLcNZUJKDGRGwAQf6rWtm3FegUgIpjbuuiLuQrdgoAs9E9sbJGnzp4eJ4hyeCDvnWZEZNjm0QvZ1D9VZy1Hy15PkpmY1ABy+2YO8C4Me6Gi19qDtvEih7MQybz3o1sqbtm0bR401Wjc3lbIfKKXkitfR8VVyeiaSnztzoqzKPS2J3RjOtz0eDVBmVU+CHJcOEKdxP+5B19IT8Lls2SBu8dnsiwHDJHnffKF04w3ZqN78J0NvUm5Tm/sgdv9cmmv50rZgDI/mdZVrTTVdw1DKYbhkReD9nxkvrJ4Pdur5GxCDPO3iXiXmemWN+S2IIoenn5RjdRjP5mSbmv/5QrZdFcYvCbdFpR1vD9Z3rg/pvHA/ZMLqJchZLKsZOns3oIiwm0CXK5VqkbHZai8dMEcbGopTp6/9W43AVSBf79xDA==',
    'SRT5': '1734964517',
    '_naver_usersession_': 'Xy+KgqEqtZbb4u4UHrbB8xt6',
    'page_uid': 'i2D3ilqo1SCssiCLmWKssssstpC-253595',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    'landHomeFlashUseYn': 'Y',
    'realestate.beta.lastclick.cortar': '4700000000',
    'REALESTATE': 'Mon%20Dec%2023%202024%2023%3A45%3A18%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'BUC': 'yhQ3wufDP1pBGVb_wwCg9ZJXk0JujGL2z5TtPYgHBdA=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MzQ5NjUxMTgsImV4cCI6MTczNDk3NTkxOH0.jwM5wFLmsKXRZltPwqIzqxnnM7GSz5DEkvoEwObSfLY',
    # 'cookie': 'NSCS=1; ASID=de6d3fad0000018bfc266dd600000045; _ga_1THKVZ9Q8W=GS1.1.1701436392.2.0.1701436392.60.0.0; _fwb=167zEj593YWD8Oauc7eODSo.1702433942332; _tt_enable_cookie=1; _ttp=S2T9izlEqdWxCxZjwxzhGvEh1_m; _ga_4BKHBFKFK0=GS1.1.1705152462.1.1.1705152467.55.0.0; _fwb=186lnNd66PWfMIvZbL8TEbj.1708260296889; NNB=PO5L5IZFRDQWK; NFS=2; m_loc=8ff896e91706fbc1adddcab7477a096fcee741096725b1e6c8d8658cc217a7b6a09e33d6988982b14dbf50ce9098692a; _ga_EFBDNNF91G=GS1.1.1720251571.1.0.1720251577.0.0.0; tooltipDisplayed=true; NID_AUT=TcWpgbnbVkHD9g0UpNjuaabFaqHBmUZHPv5VE15AZ4LbJ0fRrB9yu8bcaRoy5/qe; NID_JKL=YcZdBhtCO7Jb799V9+lWMCRcpFX5KUXPIcLvRLUg5NM=; recent_card_list=10226; BNB_FINANCE_HOME_TOOLTIP_MYASSET=true; wcs_bt=4f99b5681ce60:1733033164; _fbp=fb.1.1733047589437.621516362542158689; _ga_451MFZ9CFM=GS1.1.1733054846.2.1.1733054868.0.0.0; _fbc=fb.1.1733400349477.PAZXh0bgNhZW0CMTEAAaaOhgY-O2C8KNMdIXXqvg6aLgz-WbRpldObuvuGT_nmHWRTDd0vEYyDScA_aem_ikeqAQKr5-_AIDJqJcBIOA; _ga=GA1.2.1213673474.1701432613; _ga_6Z6DP60WFK=GS1.2.1734093180.3.0.1734093180.60.0.0; NAC=1IyjBQAPbIAO; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDA2MzU="; NV_WETR_LOCATION_RGN_M="MDkxNDA2MzU="; NACT=1; SRT30=1734944705; NID_SES=AAAB2Is8JNlbUbZ9296Dh6mQqsQO3FW1Bno6RUSJqUevhqGTHnAnsA4C4XLumwmWz9MFkMpkav2XBXrjEy0+zc82EJOnV1IVEOtPxaYHE/q26HfGH7YwT+7kRYFXHwiN9810P08+FRJdXuzWZRyyrSk/W9DVOa9IvreZqFdOuBc85oR2fmfCBQdd/xBcdYYm/5QNKudMKKa8ZKnKeDwLBT0TlRL5HhLcNZUJKDGRGwAQf6rWtm3FegUgIpjbuuiLuQrdgoAs9E9sbJGnzp4eJ4hyeCDvnWZEZNjm0QvZ1D9VZy1Hy15PkpmY1ABy+2YO8C4Me6Gi19qDtvEih7MQybz3o1sqbtm0bR401Wjc3lbIfKKXkitfR8VVyeiaSnztzoqzKPS2J3RjOtz0eDVBmVU+CHJcOEKdxP+5B19IT8Lls2SBu8dnsiwHDJHnffKF04w3ZqN78J0NvUm5Tm/sgdv9cmmv50rZgDI/mdZVrTTVdw1DKYbhkReD9nxkvrJ4Pdur5GxCDPO3iXiXmemWN+S2IIoenn5RjdRjP5mSbmv/5QrZdFcYvCbdFpR1vD9Z3rg/pvHA/ZMLqJchZLKsZOns3oIiwm0CXK5VqkbHZai8dMEcbGopTp6/9W43AVSBf79xDA==; SRT5=1734964517; _naver_usersession_=Xy+KgqEqtZbb4u4UHrbB8xt6; page_uid=i2D3ilqo1SCssiCLmWKssssstpC-253595; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; landHomeFlashUseYn=Y; realestate.beta.lastclick.cortar=4700000000; REALESTATE=Mon%20Dec%2023%202024%2023%3A45%3A18%20GMT%2B0900%20(Korean%20Standard%20Time); BUC=yhQ3wufDP1pBGVb_wwCg9ZJXk0JujGL2z5TtPYgHBdA=',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/797?ms=37.560164,127.021751,17&a=APT:PRE:ABYG:JGC&e=RETAIL',
    'sec-ch-ua': '"Chromium";v="130", "Whale";v="4", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Whale/4.29.282.14 Safari/537.36',
}

# Function to get data from the API for pages 1 to 10
@st.cache_data
def fetch_all_data():
    all_articles = []
    for page in range(1, 11):
        try:
            # Make the request for the specific page
            url = f'https://new.land.naver.com/api/articles/complex/111515?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount=300&maxHouseHoldCount&showArticle=false&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page={page}&complexNo=111515&buildingNos=&areaNos=&type=list&order=prc'
            response = requests.get(url, cookies=cookies, headers=headers)

            # Verify response is valid JSON
            if response.status_code == 200:
                data = response.json()
                articles = data.get("articleList", [])
                all_articles.extend(articles)
            else:
                st.warning(f"Failed to retrieve data for page {page}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
        except ValueError:
            st.error(f"Non-JSON response for page {page}.")

    return all_articles

# Fetch data for all pages
data = fetch_all_data()

# Transform data into a DataFrame if data is available
if data:
    df = pd.DataFrame(data)
    # Select columns to display
    df_display = df[["articleNo", "articleName", "realEstateTypeName", "tradeTypeName", "floorInfo",
                     "dealOrWarrantPrc", "areaName", "direction", "articleConfirmYmd", "articleFeatureDesc",
                     "tagList", "buildingName", "sameAddrMaxPrc", "sameAddrMinPrc", "realtorName"]]

    # Display the table in Streamlit with a clean, readable layout
    st.write("### Real Estate Listings - Pages 1 to 10")
    st.dataframe(df_display)
else:
    st.write("No data available.")
