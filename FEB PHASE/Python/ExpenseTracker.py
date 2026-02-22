class ExpenseValidationError(Exception):
    pass
class ExpenseManager:
    def __init__(self,):
        self.__expenses =[]
    @staticmethod
    def validate_user_id(user_id):
        if isinstance(user_id, bool) or not isinstance(user_id, int):
            raise ExpenseValidationError("Invalid user_id.")
    @staticmethod
    def validate_Amount(amount):
        if isinstance(amount, bool) or not isinstance(amount, (int,float)):
            raise ExpenseValidationError("Invalid Amount.")
        if amount <= 0:
            raise ExpenseValidationError("Amount must be greater than 0.")
    @staticmethod
    def validate_Category(category):
        if not isinstance(category, str) or not category.strip():
            raise ExpenseValidationError("Invalid category.")
    
    def add_expense(self,user_id,amount,category):
        self.validate_Amount(amount)
        self.validate_user_id(user_id)
        self.validate_Category(category)
        self.__expenses.append({
            'User Id': user_id,
            'Amount': amount,
            'Category': category
        })
    def get_total_expense(self,user_id):
        self.validate_user_id(user_id)
        total_expense = 0
        for expense in self.__expenses:
            if expense['User Id'] == user_id:
                total_expense += expense['Amount']
        return total_expense
    def get_category_expense(self,user_id,category):
        self.validate_user_id(user_id)
        self.validate_Category(category)
        category_expense = 0
        for i in self.__expenses:
            if i['User Id'] == user_id and i['Category'] == category:
                category_expense += i['Amount']
        return category_expense
    def get_all_expenses(self,user_id):
        self.validate_user_id(user_id)
        return [expense.copy() for expense in self.__expenses if expense["User Id"] == user_id]