class TransactionValidationError(Exception):
    pass
class TransactionLogger:
    @staticmethod
    def __validate_user_id(user_id):
        if not isinstance(user_id,int) or isinstance(user_id,bool):
            raise TransactionValidationError('Invalid user_id.')
    @staticmethod
    def __validate_amount(amount):
        if not isinstance(amount,(int,float)) or isinstance(amount,bool) or amount<=0:
            raise TransactionValidationError('Invalid Amount')
    @staticmethod
    def __validate_type(txn_type):
        if txn_type not in ('credit','debit'):
            raise TransactionValidationError('Invalid type')
    def __init__(self):
        self.__transactions=[]
    def add_transaction(self,user_id, amount, txn_type):
        self.__validate_user_id(user_id)
        self.__validate_amount(amount)
        self.__validate_type(txn_type)
        transaction = {
            'user_id': user_id,
            'amount': float(amount),
            'type': txn_type
        }
        self.__transactions.append(transaction)
    
    def get_user_balance(self,user_id):
        self.__validate_user_id(user_id)
        balance =0.0
        for txn in self.__transactions:
            if txn['user_id'] == user_id:
                if txn['type'] == 'credit':
                    balance += txn['amount']
                else:
                    balance -= txn['amount']
        return balance
    
    def get_all_transactions(self,user_id):
        self.__validate_user_id(user_id)
        return [transaction.copy() for transaction in self.__transactions if transaction['user_id'] == user_id]