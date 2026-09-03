from abc import ABC, abstractmethod
from datetime import datetime


class Transaction(ABC):
    """Base class for all financial transactions."""

    def __init__(self, transaction_id, amount, description, category, date=None):
        self.transaction_id = transaction_id
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Transaction ID must be a positive integer.")
        self._transaction_id = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError("Amount must be a number.")

        if value <= 0:
            raise ValueError("Amount must be greater than zero.")

        self._amount = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Description cannot be empty.")
        self._description = value.strip()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Category cannot be empty.")
        self._category = value.strip().title()

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be YYYY-MM-DD.")
        self._date = value

    @property
    @abstractmethod
    def transaction_type(self):
        """Return transaction type."""

    @abstractmethod
    def calculate_effect(self):
        """Return how this transaction affects balance."""

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "amount": self.amount,
            "description": self.description,
            "category": self.category,
            "date": self.date,
            "transaction_type": self.transaction_type,
        }

    def __str__(self):
        return (
            f"[{self.transaction_id}] "
            f"{self.date} | "
            f"{self.transaction_type.upper():7} | "
            f"{self.category:15} | "
            f"{self.amount:.2f} | "
            f"{self.description}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.transaction_id}, "
            f"amount={self.amount}, "
            f"category='{self.category}', "
            f"date='{self.date}')"
        )

    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return NotImplemented
        return self.transaction_id == other.transaction_id

    def __lt__(self, other):
        if not isinstance(other, Transaction):
            return NotImplemented
        return self.amount < other.amount
