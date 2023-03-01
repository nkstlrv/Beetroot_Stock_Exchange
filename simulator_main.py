import json
import yfinance as yf


class Exchange:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.data = self.load_data()
        self.portfolio = self.data["portfolio"]

    @staticmethod
    def get_price(ticker: str):
        try:
            return yf.Ticker(ticker).fast_info["lastPrice"]
        except KeyError:
            raise KeyError("You are trying to find a non-existing ticker")

    def sell(self, ticker: str, amount: int):
        ticker = ticker.upper()
        amount = int(amount)

        # Checking if enough tickers in portfolio
        if ticker not in self.portfolio:
            print("You do not have this ticker")
            return False
        elif self.portfolio[ticker] < amount:
            print("Not enough tickers")
            return False

        # If OK performing the transaction
        sell_transaction = self.get_price(ticker) * amount
        self.portfolio[ticker] -= amount
        self.data['balance'] += round(sell_transaction, 3)
        self.save_data()
        print("Successful SELL transaction")
        return True

    def buy(self, ticker: str, amount: int):
        ticker = ticker.upper()
        amount = int(amount)

        # Calculating the transaction cost
        try:
            transaction_cost = self.get_price(ticker) * amount
        except KeyError:
            print("You are trying to buy a non-existing ticker")
            return False

        # Checking if you can afford it
        if self.data['balance'] - transaction_cost < 0:
            print("You can not afford it")
            return False

        # If everything is OK performing the transaction
        if ticker in self.portfolio.keys():
            self.portfolio[ticker] += amount
        else:
            self.portfolio[ticker] = amount
        self.data['balance'] -= round(transaction_cost, 3)
        self.save_data()
        print("Successful BUY transaction")
        return True

    def load_data(self) -> dict:
        with open(self.path_to_file, "r+") as ld:
            my_data = json.load(ld)
            return my_data

    def save_data(self):
        with open(self.path_to_file, "w") as sd:
            json.dump(self.data, sd)

    def valid_balance(self, amount: int):
        pass

    def valid_ticker_balance(self, ticker: str, amount: int):
        pass

    def __str__(self):
        info = f"{'=' * 35}" \
                f"\nYour Portfolio & Balance:" \
                f"\n Funds available --> {round(self.data['balance'], 3)} USD" \
                f"\n ticker --> amount"
        for k, v in self.portfolio.items():
            info += f"\n   {k} --> {v}"
        info += f"\n{'=' * 35}"
        return info


if __name__ == "__main__":
    ex_1 = Exchange(r"Data\my_data.json")
    print(ex_1)




