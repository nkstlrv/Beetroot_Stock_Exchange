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


    def buy(self, ticker: str, buy_amount: int):
        ticker = ticker.upper()
        buy_amount = int(buy_amount)

        # Calculating the transaction cost
        try:
            buy_transaction_cost = self.get_price(ticker) * buy_amount
        except KeyError:
            print("You are trying to buy a non-existing ticker")
            return False

        # Checking if you can afford it
        if self.data['balance'] - buy_transaction_cost < 0:
            print("Not enough balance")
            return False

        # If everything is OK performing the transaction
        if ticker in self.portfolio.keys():
            self.portfolio[ticker] += buy_amount
        else:
            self.portfolio[ticker] = buy_amount
        self.data['balance'] -= round(buy_transaction_cost, 3)
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


    # Don't actually know how to use this validate method
    def valid_balance(self, amount: int):
        pass


    # The same for this one
    def valid_ticker_balance(self, ticker: str, amount: int):
        pass


    def __str__(self):
        info = f"{'=' * 35}" \
                f"\n\t\tPORTFOLIO & BALANCE\n" \
               f"{'=' * 35}" \
                f"\n Balance --> {round(self.data['balance'], 3)} USD\n" \
               f"{'-' * 25}" \
                f"\n Portfolio:\n" \
               f"{'-' * 25}"
        for k, v in self.portfolio.items():
            info += f"\n{k} --> {v}"
        return info


if __name__ == "__main__":
    ex_1 = Exchange(r"Data\my_data.json")
    print(ex_1)




