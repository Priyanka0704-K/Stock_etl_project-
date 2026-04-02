import yfinance as yf
import pandas as pd

def extract(stock="AAPL"):
    data = yf.download(stock, period="6mo")
    data.reset_index(inplace=True)
    return data

def transform(data):
    data['MA50'] = data['Close'].rolling(50).mean()
    data['MA100'] = data['Close'].rolling(100).mean()
    data['Daily_Return'] = data['Close'].pct_change()
    data.dropna(inplace=True)
    return data

def load(data):
    data.to_csv("../data/stock_data.csv", index=False)

if __name__ == "__main__":
    df = extract("AAPL")
    df = transform(df)
    load(df)
    print("ETL Completed")
