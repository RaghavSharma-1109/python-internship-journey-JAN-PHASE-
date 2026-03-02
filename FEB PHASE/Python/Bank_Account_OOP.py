class InsufficientFundsError(Exception):
    pass
class InvalidAmountError(Exception):
    pass
class BankAccount:
    total_account = 0
    @classmethod
    def validate_amount(amount):
        if not isinstance(amount,(int,float)) or isinstance(amount,bool):
            raise InvalidAmountError(
                f"Invalid Amount Type"
            )
        if amount<0:
            raise InvalidAmountError(f"Amount must be greater than 0")
    def __init__(self,initial_balance) -> None:
        BankAccount.validate_amount(initial_balance)
        self.__balance = initial_balance
        self.transaction_list = []
        BankAccount.total_account += 1

    def deposit(self,amount):
        BankAccount.validate_amount(amount)
        self.__balance+=amount
        transaction = ('deposit',amount)
        self.transaction_list.append(transaction)
    
    def withdraw(self,amount):
        BankAccount.validate_amount(amount)
        if amount>self.__balance:
            raise InsufficientFundsError(f"Insufficient balance to withdraw")
        self.__balance -= amount
        transaction = ('withdraw',amount)
        self.transaction_list.append(transaction)
    
    def get_balance(self):
        return copy(self.__balance)