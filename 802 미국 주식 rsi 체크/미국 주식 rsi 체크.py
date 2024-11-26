import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
import io


def get_nasdaq_symbols():
    """
    나스닥 주요 종목 심볼 리스트를 반환합니다.
    """
    # 주요 나스닥 종목들의 리스트
    stocks = {
        # 기술주
        'AAPL': 'Apple Inc.',
        'MSFT': 'Microsoft Corporation',
        'GOOGL': 'Alphabet Inc.',
        'GOOG': 'Alphabet Inc.',
        'META': 'Meta Platforms Inc.',
        'NVDA': 'NVIDIA Corporation',
        'AMZN': 'Amazon.com Inc.',
        'TSLA': 'Tesla Inc.',
        'AMD': 'Advanced Micro Devices Inc.',
        'INTC': 'Intel Corporation',
        'CSCO': 'Cisco Systems Inc.',
        'ADBE': 'Adobe Inc.',
        'NFLX': 'Netflix Inc.',
        'CRM': 'Salesforce Inc.',

        # 반도체
        'AVGO': 'Broadcom Inc.',
        'QCOM': 'QUALCOMM Incorporated',
        'MU': 'Micron Technology Inc.',
        'TXN': 'Texas Instruments Inc.',
        'AMAT': 'Applied Materials Inc.',
        'LRCX': 'Lam Research Corporation',

        # 소프트웨어/클라우드
        'NOW': 'ServiceNow Inc.',
        'WDAY': 'Workday Inc.',
        'ZS': 'Zscaler Inc.',
        'DDOG': 'Datadog Inc.',
        'SNOW': 'Snowflake Inc.',
        'NET': 'Cloudflare Inc.',

        # 전기차/자율주행
        'RIVN': 'Rivian Automotive Inc.',
        'LCID': 'Lucid Group Inc.',
        'MDB': 'MongoDB Inc.',

        # 바이오/헬스케어
        'MRNA': 'Moderna Inc.',
        'BNTX': 'BioNTech SE',
        'REGN': 'Regeneron Pharmaceuticals Inc.',
        'ILMN': 'Illumina Inc.',
        'VRTX': 'Vertex Pharmaceuticals Inc.',

        # 금융/핀테크
        'PYPL': 'PayPal Holdings Inc.',
        'COIN': 'Coinbase Global Inc.',
        'HOOD': 'Robinhood Markets Inc.',
        'SOFI': 'SoFi Technologies Inc.',

        # 커뮤니케이션
        'ZM': 'Zoom Video Communications Inc.',
        'TEAM': 'Atlassian Corporation',
        'OKTA': 'Okta Inc.',

        # 소비자
        'ABNB': 'Airbnb Inc.',
        'UBER': 'Uber Technologies Inc.',
        'DASH': 'DoorDash Inc.',
        'ROKU': 'Roku Inc.',
        'SHOP': 'Shopify Inc.',

        # 기타
        'PANW': 'Palo Alto Networks Inc.',
        'CRWD': 'CrowdStrike Holdings Inc.',
        'FTNT': 'Fortinet Inc.',
        'TTD': 'The Trade Desk Inc.',
        'RBLX': 'Roblox Corporation'
    }

    print(f"총 {len(stocks)}개의 나스닥 종목을 분석합니다.")
    return stocks


def calculate_rsi(data, periods=14):
    """
    주가 데이터로부터 RSI를 계산합니다.
    """
    delta = data.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=periods).mean()
    avg_loss = loss.rolling(window=periods).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


def screen_stocks_by_rsi(target_rsi, threshold=5, period='1mo'):
    """
    지정된 RSI 값 주변의 주식들을 스크리닝합니다.
    """
    stocks_dict = get_nasdaq_symbols()
    results = []
    total = len(stocks_dict)

    print(f"\n전체 {total}개 종목 분석 시작...")

    for idx, (symbol, company_name) in enumerate(stocks_dict.items(), 1):
        if idx % 10 == 0:  # 진행상황 표시
            print(f"진행중: {idx}/{total} ({(idx / total * 100):.1f}%)")

        try:
            # 주가 데이터 다운로드
            stock = yf.Ticker(symbol)
            hist = stock.history(period=period)

            if len(hist) < 14:  # RSI 계산에 필요한 최소 데이터 확인
                continue

            # RSI 계산
            current_rsi = calculate_rsi(hist['Close']).iloc[-1]

            # 목표 RSI 범위 내에 있는지 확인
            if abs(current_rsi - target_rsi) <= threshold:
                # 기업 정보 가져오기
                info = stock.info
                current_price = hist['Close'].iloc[-1]
                prev_price = hist['Close'].iloc[-2]
                price_change = ((current_price - prev_price) / prev_price) * 100

                results.append({
                    'Symbol': symbol,
                    'Company': company_name,
                    'Current_Price': f"${current_price:.2f}",
                    'Price_Change': f"{price_change:+.2f}%",
                    'RSI': round(current_rsi, 2),
                    'Volume': f"{int(hist['Volume'].iloc[-1]):,}",
                    'Market_Cap': info.get('marketCap', 0),
                    'Industry': info.get('industry', 'N/A'),
                })
                print(f"\n발견: {symbol} (RSI: {round(current_rsi, 2)}, 가격변동: {price_change:+.2f}%)")

        except Exception as e:
            continue

    # 결과를 DataFrame으로 변환하고 RSI 기준으로 정렬
    results_df = pd.DataFrame(results)
    if not results_df.empty:
        # Market Cap을 보기 좋게 포맷팅
        results_df['Market_Cap'] = results_df['Market_Cap'].apply(
            lambda x: f"${x / 1e9:.2f}B" if x >= 1e9 else (f"${x / 1e6:.2f}M" if x > 0 else "N/A")
        )
        results_df = results_df.sort_values('RSI')

    return results_df


def main():
    """
    메인 실행 함수
    """
    print("나스닥 주요 종목 RSI 스크리너 시작...")

    # 사용자 입력 받기
    while True:
        try:
            target_rsi = float(input("\n목표 RSI 값을 입력하세요 (0-100): "))
            if 0 <= target_rsi <= 100:
                break
            print("RSI는 0에서 100 사이의 값이어야 합니다.")
        except ValueError:
            print("올바른 숫자를 입력해주세요.")

    while True:
        try:
            threshold = float(input("RSI 허용 범위를 입력하세요 (예: 5): "))
            if threshold > 0:
                break
            print("허용 범위는 양수여야 합니다.")
        except ValueError:
            print("올바른 숫자를 입력해주세요.")

    print("\n스크리닝 시작...")
    results = screen_stocks_by_rsi(target_rsi, threshold)

    if results.empty:
        print("\n조건에 맞는 종목을 찾지 못했습니다.")
    else:
        print(f"\n총 {len(results)}개 종목이 조건에 맞습니다:")
        # 결과 출력 시 컬럼 순서 지정
        columns = ['Symbol', 'Company', 'Current_Price', 'Price_Change', 'RSI', 'Volume', 'Market_Cap', 'Industry']
        print(results[columns].to_string(index=False))

        # 결과를 CSV 파일로 저장
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"nasdaq_rsi_screening_{timestamp}.csv"
        results.to_csv(filename, index=False)
        print(f"\n결과가 {filename}에 저장되었습니다.")


if __name__ == "__main__":
    main()