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

    @property
    def set_balance(self, value):
        if value < 0:
            print("Please enter a positive value to set the account balance.")
            return
        self.__balance = value
