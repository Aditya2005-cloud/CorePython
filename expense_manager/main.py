from models import User
from services import TransactionService, BudgetService, ReportService
from storage import JSONStorage, CSVStorage
from utils.helpers import format_currency


def print_transactions(transactions):
    if not transactions:
        print("\nNo transactions found.")
        return

    print("\n" + "=" * 90)
    print("TRANSACTIONS")
    print("=" * 90)

    for transaction in transactions:
        print(transaction)


def transaction_menu(user):
    service = TransactionService(user)

    while True:
        print("\n========== TRANSACTIONS ==========")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Search")
        print("5. Sort")
        print("6. Delete")
        print("7. Back")

        choice = input("Choose: ")

        try:
            if choice == "1":
                amount = float(input("Amount: "))
                description = input("Description: ")
                category = input("Category: ")
                date = input("Date (YYYY-MM-DD): ")

                transaction = service.add_income(amount, description, category, date)

                print("\nIncome added:")
                print(transaction)

            elif choice == "2":
                amount = float(input("Amount: "))
                description = input("Description: ")
                category = input("Category: ")
                date = input("Date (YYYY-MM-DD): ")

                transaction = service.add_expense(amount, description, category, date)

                print("\nExpense added:")
                print(transaction)

            elif choice == "3":
                print_transactions(service.get_all())

            elif choice == "4":
                keyword = input("Search keyword: ")
                results = service.search(keyword)
                print_transactions(results)

            elif choice == "5":
                print("\n1. Amount")
                print("2. Date")
                print("3. Category")

                sort_choice = input("Choose field: ")
                fields = {"1": "amount", "2": "date", "3": "category"}

                if sort_choice not in fields:
                    print("Invalid choice.")
                    continue

                reverse = input("Descending? (y/n): ").lower() == "y"
                results = service.sort_by(fields[sort_choice], reverse)
                print_transactions(results)

            elif choice == "6":
                transaction_id = int(input("Transaction ID: "))
                deleted = service.delete_transaction(transaction_id)
                print(f"Deleted: {deleted}")

            elif choice == "7":
                break

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print(f"Error: {error}")


def budget_menu(user):
    service = BudgetService(user)

    while True:
        print("\n========== BUDGETS ==========")
        print("1. Create Budget")
        print("2. View Budgets")
        print("3. Budget Status")
        print("4. Back")

        choice = input("Choose: ")

        try:
            if choice == "1":
                category = input("Category: ")
                limit = float(input("Budget limit: "))
                month = int(input("Month: "))
                year = int(input("Year: "))

                budget = service.create_budget(category, limit, month, year)

                print("\nBudget created:")
                print(budget)

            elif choice == "2":
                if not user.budgets:
                    print("\nNo budgets.")
                    continue

                for budget in user.budgets:
                    print(budget)

            elif choice == "3":
                if not user.budgets:
                    print("\nNo budgets.")
                    continue

                for budget in user.budgets:
                    status = service.get_status(budget)

                    print("\n--------------------------")
                    print(f"Category: {status['category']}")
                    print(f"Budget: {format_currency(status['budget'])}")
                    print(f"Spent: {format_currency(status['spent'])}")
                    print(f"Remaining: {format_currency(status['remaining'])}")
                    print(f"Usage: {status['percentage']:.2f}%")

                    if status["exceeded"]:
                        print("STATUS: EXCEEDED")
                    else:
                        print("STATUS: OK")

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print(f"Error: {error}")


def report_menu(user):
    report_service = ReportService(user.transactions)
    csv_storage = CSVStorage()

    while True:
        print("\n========== REPORTS ==========")
        print("1. Monthly Report")
        print("2. Category Report")
        print("3. Highest Expenses")
        print("4. Export CSV")
        print("5. Back")

        choice = input("Choose: ")

        try:
            if choice == "1":
                month = int(input("Month: "))
                year = int(input("Year: "))

                report = report_service.monthly_report(month, year)

                print("\n========== MONTHLY REPORT ==========")
                print("Income:", format_currency(report["income"]))
                print("Expense:", format_currency(report["expense"]))
                print("Savings:", format_currency(report["savings"]))

            elif choice == "2":
                report = report_service.category_report()

                print("\n========== CATEGORY REPORT ==========")
                for category, amount in report.items():
                    print(f"{category:20}{format_currency(amount)}")

            elif choice == "3":
                expenses = report_service.highest_expenses()

                print("\n========== HIGHEST EXPENSES ==========")
                print_transactions(expenses)

            elif choice == "4":
                csv_storage.export_transactions("transactions.csv", user.transactions)
                print("\nCSV exported to reports/")

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print(f"Error: {error}")


def save_user_data(user):
    storage = JSONStorage()

    storage.save("users.json", [user.to_dict()])
    storage.save("transactions.json", [transaction.to_dict() for transaction in user.transactions])
    storage.save("budgets.json", [budget.to_dict() for budget in user.budgets])


def main():
    print("=" * 50)
    print("       PERSONAL EXPENSE MANAGER")
    print("=" * 50)

    name = input("Enter your name: ")
    username = input("Enter username: ")

    user = User(1, name, username)

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Transactions")
        print("2. Budgets")
        print("3. Reports")
        print("4. Account Summary")
        print("5. Save")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            transaction_menu(user)

        elif choice == "2":
            budget_menu(user)

        elif choice == "3":
            report_menu(user)

        elif choice == "4":
            service = TransactionService(user)

            print("\n========== ACCOUNT SUMMARY ==========")
            print("Income:", format_currency(service.total_income()))
            print("Expenses:", format_currency(service.total_expense()))
            print("Balance:", format_currency(service.balance()))
            print("Transactions:", len(user))

        elif choice == "5":
            save_user_data(user)
            print("\nData saved successfully.")

        elif choice == "6":
            save_user_data(user)
            print("\nData saved. Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
