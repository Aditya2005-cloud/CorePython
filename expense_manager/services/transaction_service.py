from models import Income, Expense
from utils.helpers import generate_id


class TransactionService:
    def __init__(self, user):
        self.user = user

    def add_income(self, amount, description, category, date=None):
        transaction_id = generate_id(self.user.transactions, "transaction_id")

        income = Income(transaction_id, amount, description, category, date)
        self.user.add_transaction(income)
        return income

    def add_expense(self, amount, description, category, date=None):
        transaction_id = generate_id(self.user.transactions, "transaction_id")

        expense = Expense(transaction_id, amount, description, category, date)
        self.user.add_transaction(expense)
        return expense

    def delete_transaction(self, transaction_id):
        return self.user.remove_transaction(transaction_id)

    def get_all(self):
        return self.user.transactions

    def search(self, keyword):
        keyword = keyword.lower()

        return [
            transaction
            for transaction in self.user.transactions
            if keyword in transaction.description.lower()
            or keyword in transaction.category.lower()
        ]

    def filter_transactions(self, **filters):
        transactions = self.user.transactions

        if "transaction_type" in filters:
            transactions = [
                t for t in transactions if t.transaction_type == filters["transaction_type"]
            ]

        if "category" in filters:
            transactions = [
                t for t in transactions if t.category.lower() == filters["category"].lower()
            ]

        if "month" in filters:
            transactions = [
                t for t in transactions if int(t.date[5:7]) == int(filters["month"])
            ]

        if "year" in filters:
            transactions = [
                t for t in transactions if int(t.date[:4]) == int(filters["year"])
            ]

        return transactions

    def sort_by(self, field, reverse=False):
        valid_fields = {
            "amount": lambda t: t.amount,
            "date": lambda t: t.date,
            "category": lambda t: t.category,
            "description": lambda t: t.description,
        }

        if field not in valid_fields:
            raise ValueError("Invalid sorting field.")

        return sorted(self.user.transactions, key=valid_fields[field], reverse=reverse)

    def total_income(self):
        return sum(t.amount for t in self.user.transactions if t.transaction_type == "income")

    def total_expense(self):
        return sum(t.amount for t in self.user.transactions if t.transaction_type == "expense")

    def balance(self):
        return sum(t.calculate_effect() for t in self.user.transactions)
