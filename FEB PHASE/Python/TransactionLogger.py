class TransactionLogger:
    def __init__(self):
        self.transactions = []
        self._next_id =1
    def add_transaction(self, data: dict)
        if type(data) is not dict:
            return {
                    "status": False,
                    "message": "Data must be of dict type",
                    "data": None
                }
            
        req = {'user_id','amount','type'}
        if not req.issubset(data):
            return {
                    "status": False,
                    "message": "Missing required fields",
                    "data": None
                }
        user_id = data.get('user_id')
        if isinstance(user_id, bool) or not isinstance(user_id, int):
            return {
                    "status": False,
                    "message": "User ID must be integer.",
                    "data": None
                }
        amount = data.get('amount')
        if type(amount) is not int and type(amount) is not float:
            return {
                    "status": False,
                    "message": "Amount must be of tyoe of integer or float",
                    "data": None
                }
        type_trans = data.get('type')
        if type(type_trans) is not str:
            return {
                    "status": False,
                    "message": "Type of transaction must be a string",
                    "data": None
                }
        if type_trans not in ['credit','debit']:
            return {
                    "status": False,
                    "message": "Transaction must be of credit or debit",
                    "data": None
                }
        transaction = {
            "transaction_id": self._next_id,
            "user_id": user_id,
            "amount": float(amount),
            "type": type_trans
        }

        self.transactions.append(transaction)
        self._next_id += 1
        return {
            "status": True,
            "message": "Transaction Added",
            "data": transaction
        }

    def get_user_transactions(self,user_id):
        if type(user_id) is not int:
            return {
                    "status": False,
                    "message": "User Id must be Integer",
                    "data": None
                }
        user_txns = [t for t in self.transactions if t["user_id"] == user_id]
        return {
            "status": True,
            "message": "User transactions fetched",
            "data": user_txns
        }
    def get_user_balance(self,user_id):
        if type(user_id) is not int:
            return {
                    "status": False,
                    "message": "User Id must be Integer",
                    "data": None
                }
        user_txns = [t for t in self.transactions if t["user_id"] == user_id]

        balance = 0
        for i in user_txns:
            if i['type'] == 'credit':
                balance += i['amount']
            elif i['type'] == 'debit':
                balance -= i['amount']
        
        return{
            "status": True,
            "message": "User balance calculated",
            "data": balance
        }