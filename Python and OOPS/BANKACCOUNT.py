class Account:
    bank_name = "State Bank of India"   # class variable

    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, holder_name, balance, interest_rate):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate

    def get_balance(self):
        interest = self.balance * (self.interest_rate / 100)
        return self.balance + interest
