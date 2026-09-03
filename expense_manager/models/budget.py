class Budget:
    def __init__(self, category, limit, month, year):
        self.category = category.title()
        self.limit = float(limit)
        self.month = int(month)
        self.year = int(year)

        if self.limit <= 0:
            raise ValueError("Budget limit must be greater than zero.")

        if not 1 <= self.month <= 12:
            raise ValueError("Month must be between 1 and 12.")

    def calculate_remaining(self, transactions):
        spent = sum(
            transaction.amount
            for transaction in transactions
            if (
                transaction.transaction_type == "expense"
                and transaction.category == self.category
                and transaction.date[:7] == f"{self.year:04d}-{self.month:02d}"
            )
        )
        return self.limit - spent

    def is_exceeded(self, transactions):
        return self.calculate_remaining(transactions) < 0

    def usage_percentage(self, transactions):
        spent = self.limit - self.calculate_remaining(transactions)
        return (spent / self.limit) * 100

    def to_dict(self):
        return {
            "category": self.category,
            "limit": self.limit,
            "month": self.month,
            "year": self.year,
        }

    def __str__(self):
        return f"{self.category} | Budget: {self.limit:.2f} | {self.month:02d}/{self.year}"

    def __repr__(self):
        return (
            f"Budget(category='{self.category}', limit={self.limit}, "
            f"month={self.month}, year={self.year})"
        )
