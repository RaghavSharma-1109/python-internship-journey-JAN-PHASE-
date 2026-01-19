
class Bank_Account():
    def __init__(self,Account_holder, balance):
        self.Name = Account_holder
        self.Balance = balance
        if self.Balance < 0:
            return ValueError
    def deposit(self, amount):
        if amount<=0:
            return "Invalid Deposit Amount"
        else:
            self.Balance += amount
            return 'Deposit successful'
    def withdraw(self, amount):
        if amount<=0:
            return 'Invalid Withdrawal ammount'
        elif amount > self.Balance:
            return 'Insufficient Balance'
        else:
            self.Balance -= amount
    def display(self):
        print(f'Account Holder: {self.Name}; Balance:{self.Balance}')

emp1 = Bank_Account('Raghav', 1000000)
emp1.deposit(20000)
emp1.withdraw(10000)      
emp1.display()  