 
class Expense():
    def __init__(self, id, description, amount, date=None):
        self.id = id
        self.description = description
        self.amount = amount
        self.date = date