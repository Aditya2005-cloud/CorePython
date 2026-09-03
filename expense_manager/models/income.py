from .transaction import Transaction


class Income(Transaction):
    @property
    def transaction_type(self):
        return "income"

    def calculate_effect(self):
        return self.amount
