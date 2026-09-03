from collections import defaultdict


class ReportService:
    def __init__(self, transactions):
        self.transactions = transactions

    def monthly_report(self, month, year):
        transactions = [
            t
            for t in self.transactions
            if int(t.date[5:7]) == month and int(t.date[:4]) == year
        ]

        income = sum(t.amount for t in transactions if t.transaction_type == "income")
        expense = sum(t.amount for t in transactions if t.transaction_type == "expense")

        return {
            "month": month,
            "year": year,
            "income": income,
            "expense": expense,
            "savings": income - expense,
        }

    def category_report(self):
        result = defaultdict(float)

        for transaction in self.transactions:
            if transaction.transaction_type == "expense":
                result[transaction.category] += transaction.amount

        return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

    def income_categories(self):
        categories = {
            transaction.category
            for transaction in self.transactions
            if transaction.transaction_type == "income"
        }
        return categories

    def highest_expenses(self, count=5):
        expenses = [
            transaction
            for transaction in self.transactions
            if transaction.transaction_type == "expense"
        ]

        return sorted(expenses, key=lambda transaction: transaction.amount, reverse=True)[:count]

    def custom_report(self, *transactions, **filters):
        result = list(transactions)

        if filters.get("category"):
            result = [t for t in result if t.category == filters["category"]]

        if filters.get("transaction_type"):
            result = [
                t for t in result if t.transaction_type == filters["transaction_type"]
            ]

        return result
