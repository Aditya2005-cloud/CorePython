from .transaction import Transaction


class Expense(Transaction):
    @property
    def transaction_type(self):
        return "expense"

    def calculate_effect(self):
        return -self.amount
