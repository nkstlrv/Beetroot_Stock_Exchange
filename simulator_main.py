from time import sleep
import json
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

        # Calculating the cost of transaction
        try:
            ticker_price = self.get_price(ticker.upper())
            transaction_cost = ticker_price * amount
            print(f"You have bought {ticker} for ${round(transaction_cost, 3)}")
        except KeyError:
            print("You are trying to buy non-existing ticker")

        # Opening JSON
        with open(r"Data/my_data.json", "r+") as f_1:
            my_data = json.load(f_1)

        # Storing our transaction

        if my_data['balance'] - transaction_cost < 0:
            raise ValueError("Not enough funds on the account ")
        else:

            portfolio = my_data.get('portfolio')
            if portfolio.get(ticker.upper()) is None:
                my_data['portfolio'].update({ticker.upper(): amount})
            else:
                my_data['portfolio'][ticker.upper()] += amount
            my_data['balance'] -= transaction_cost
            print(my_data)

        # Loading data to JSON
        with open(r"Data/my_data.json", "w") as f_2:
            json.dump(my_data, f_2)

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

    # print(ex_1.get_price("GOOGL"))
    # print(ex_1.get_price("AAPL"))
    # print(ex_1.get_price("TSLA"))
    # print(ex_1.get_price("MSFT"))

ex_1.buy("aapl", 33)
