class User:
    def __init__(self, user_id, name, username):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.transactions = []
        self.budgets = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def remove_transaction(self, transaction_id):
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                self.transactions.remove(transaction)
                return transaction
        raise ValueError("Transaction not found.")

    def get_transaction(self, transaction_id):
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                return transaction
        return None

    def add_budget(self, budget):
        self.budgets.append(budget)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "username": self.username,
        }

    def __len__(self):
        return len(self.transactions)

    def __iter__(self):
        return iter(self.transactions)

    def __str__(self):
        return f"User: {self.name} (@{self.username}) | Transactions: {len(self)}"
