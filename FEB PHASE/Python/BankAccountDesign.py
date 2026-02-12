class BankAccount:
    def __init__(self,acc_holder_name,acc_number,initial_balance):
        if not isinstance(acc_holder_name, str):
            raise ValueError("Account holder name must be a string.")

        if isinstance(acc_number, bool) or not isinstance(acc_number, int):
            raise ValueError("Account number must be an integer.")

        if isinstance(initial_balance, bool) or not isinstance(initial_balance, (int, float)):
            raise ValueError("Initial balance must be a number.")

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.acc_holder_name = acc_holder_name
        self.acc_number = acc_number
        self._balance = initial_balance
        self._transactions = []

    
    def deposit(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            return {
                "status": False,
                "message": "Amount must be a number.",
                "data": None
            }

        if amount <= 0:
            return {
                "status": False,
                "message": "Deposit amount must be greater than zero.",
                "data": None
            }

        self._balance += amount

        transaction = {
            "type": "deposit",
            "amount": amount,
            "balance_after": self._balance
        }

        self._transactions.append(transaction)

        return {
            "status": True,
            "message": "Deposit successful.",
            "data": transaction
        }

    def withdraw(self,amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            return {
                "status": False,
                "message": "Amount must be a number.",
                "data": None
            }
        if amount <= 0:
            return {
                "status": False,
                "message": "Withdrawl amount must be greater than zero.",
                "data": None
            }
        if amount > self._balance:
            return {
                "status": False,
                "message": "Insufficient balance",
                "data": None
            }
        self._balance -= amount
        transaction = {
            "type": "Withdraw",
            "amount": amount,
            "balance_after": self._balance
        }

        self._transactions.append(transaction)

        return {
            "status": True,
            "message": "Withdrawl successful.",
            "data": transaction
        }
    def check_balance(self):
        return {
            "status": True,
            "data": {
                "balance": self._balance
                }
            }
    def get_transaction_history(self):
        return self._transactions.copy()