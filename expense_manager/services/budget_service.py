class BudgetService:
    def __init__(self, user):
        self.user = user

    def create_budget(self, category, limit, month, year):
        from models import Budget

        budget = Budget(category, limit, month, year)
        self.user.add_budget(budget)
        return budget

    def get_status(self, budget):
        transactions = self.user.transactions

        spent = budget.limit - budget.calculate_remaining(transactions)
        remaining = budget.calculate_remaining(transactions)

        return {
            "category": budget.category,
            "budget": budget.limit,
            "spent": spent,
            "remaining": remaining,
            "percentage": budget.usage_percentage(transactions),
            "exceeded": budget.is_exceeded(transactions),
        }
