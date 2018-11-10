class Account(object):
    # Has a balance, which is held in GBP. Rate is FX rate to convert to USD.

    def __init__(self, usd_rate):
        self.__balance = 0
        self.usd_rate = usd_rate

    @property
    def balance(self):
        "Returns the balance property."
        return self.__balance

    @property
    def convert(self):
        "Converts GBP balance to USD"
        return self.__balance * self.usd_rate

    @balance.setter
    def set_balance(self, value):
        if value < 0:
            print("Please enter a positive value to set the account balance.")
            return
        self.__balance = value


if __name__ == '__main__':
    account = Account(usd_rate=1.2975)
    account.set_balance = 3000
    print("Balance in GBP:", account.balance)
    print("Balance in USD:", account.convert)
    print("...trying to set negative account balance...")
    account.set_balance = -5000
    print("Balance in GBP:", account.balance)
