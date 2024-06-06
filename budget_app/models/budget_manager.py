from .expenses import Expense

class InvalidExpenseError(Exception):
    pass

class NotFoundExpenseError(Exception):
    pass


class BudgetManager:
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def add_expense(self, description, amount, date):
        if not description or amount <= 0:
            raise ValueError("Invalid Expense Data")
        
        new_expense = Expense(self.next_id, description, amount, date)
        self.expenses.append(new_expense)
        self.next_id += 1

    def get_expense(self, id):
        for expense in self.expenses:
            if expense.id == id:
                return expense
        return None

    def update_expense(self, id: int, description: str, amount: float, date):
        expense = self.get_expense(id)
        if expense:
            expense.description = description
            expense.amount = amount
            expense.date = date

    def get_expense(self, id: int):
        for expense in self.expenses:
            if expense.id == id:
                return expense
            return None
        raise NotFoundExpenseError(f"Expense id = {id} not found")

    def remove_expense(self, id: int):
        '''        
        def get_expense_description(self, id):
            expense = self.get_expense(id)
            return expense.description
        description = get_expense_description(id)'''
        expense = self.get_expense(id)
        if expense:
          self.expenses.remove(expense)
        
        #return f"{expense} has been deleted"

#update i create errors



    