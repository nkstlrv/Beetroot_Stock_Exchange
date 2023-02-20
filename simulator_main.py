from time import sleep
import yfinance as yf


class Exchange:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.data = self.load_data()
        # self.portfolio = self.data["portfolio"]
        # self.balance = self.data["balance"]

    @staticmethod
    def get_price(ticker: str):
        return round(yf.Ticker(ticker).fast_info["lastPrice"], 2)

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


if __name__ == "__main__":

    ex_1 = Exchange(r"Data\my_data.json")

    print(ex_1.get_price("GOOGL"))
    print(ex_1.get_price("AAPL"))
    print(ex_1.get_price("TSLA"))
    print(ex_1.get_price("MSFT"))
    print(ex_1.get_price("Non Existing Ticker"))

