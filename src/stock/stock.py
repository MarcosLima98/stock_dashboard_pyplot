import yfinance as yf

class stock:
    def __init__(self,ticker_name) -> None:
        self.ticker_name = self.set_ticker_name(ticker_name)

        print(self.ticker_name)


    def set_ticker_name(self,ticker_name):
        return ticker_name
