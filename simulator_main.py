from time import sleep

import yfinance as yf

# mydata.json
# {
#     "portfolio": {
#         "IBM": 100,
#         "MSFT": 10
# },
#     "balance": 100000.0
# }


class Exchange:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.data = self.load_data()
        self.portfolio = self.data["portfolio"]
        self.balance = self.data["balance"]

    @staticmethod
    def get_price(ticker: str) -> float:
        # return yf.Ticker(ticker).fast_info["lastPrice"]
        pass

    def sell(self, ticker: str, amount: int):
        pass

    def buy(self, ticker: str, amount: int):
        pass

    def load_data(self) -> dict:
        pass

    def save_data(self):
        pass

    def valid_balance(self, amount: int):
        pass

    def valid_ticker_balance(self, ticker: str, amount: int):
        pass

    def __str__(self):
        """Print balance and portfolio"""
        ...


ex = Exchange("mydata.json")

ex.buy("MSFT", 10)
sleep(10)
ex.buy("IBM", 15)
sleep(30)
ex.sell("MSFT", 5)
ex.sell("IBM", 15)

print(ex)
