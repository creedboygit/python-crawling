import yfinance as yf
import pandas as pd

def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def get_stocks_near_rsi(tickers, target_rsi, threshold=4):
    near_stocks = []
    for ticker in tickers:
        data = yf.download(ticker, period='1y')
        data['RSI'] = calculate_rsi(data)
        latest_rsi = data['RSI'].iloc[-1]
        if abs(latest_rsi - target_rsi) <= threshold:
            near_stocks.append(ticker)
            if len(near_stocks) >= 4:  # 최대 4개 종목만 추가
                break
    return near_stocks

# 나스닥 종목 리스트 가져오기
nasdaq_tickers = yf.Tickers('AAPL MSFT GOOGL AMZN FB TSLA NFLX NVDA')  # 예시로 몇 개의 종목을 사용
nasdaq_tickers = [ticker for ticker in nasdaq_tickers.tickers]  # 티커 리스트로 변환

target_rsi = float(input("원하는 RSI 값을 입력하세요: "))  # 사용자로부터 RSI 입력 받기
result = get_stocks_near_rsi(nasdaq_tickers, target_rsi)
print(result)
