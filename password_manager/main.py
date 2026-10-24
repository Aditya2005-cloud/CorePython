"""Simple command-line interface for a local password manager."""

from getpass import getpass

from models.account import load_accounts, save_accounts


def add_account() -> None:
    service = input("Service: ").strip()
    username = input("Username: ").strip()
    password = getpass("Password: ")
    if not service or not username or not password:
        print("Service, username, and password are required.")
        return

    accounts = load_accounts()
    accounts.append({"service": service, "username": username, "password": password})
    save_accounts(accounts)
    print("Account saved.")


def list_accounts() -> None:
    accounts = load_accounts()
    if not accounts:
        print("No accounts saved.")
        return
    for index, account in enumerate(accounts, start=1):
        print(f"{index}. {account['service']} — {account['username']}")


def delete_account() -> None:
    accounts = load_accounts()
    if not accounts:
        print("No accounts saved.")
        return
    list_accounts()
    try:
        index = int(input("Account number to delete: ")) - 1
    except ValueError:
        print("Enter a valid account number.")
        return
    if not 0 <= index < len(accounts):
        print("Account number is out of range.")
        return
    removed = accounts.pop(index)
    save_accounts(accounts)
    print(f"Deleted account for {removed['service']}.")


def main() -> None:
    actions = {"1": add_account, "2": list_accounts, "3": delete_account}
    while True:
        print("\nPassword Manager\n1. Add account\n2. List accounts\n3. Delete account\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "4":
            break
        action = actions.get(choice)
        if action is None:
            print("Choose an option from 1 to 4.")
            continue
        try:
            action()
        except (OSError, ValueError) as exc:
            print(f"Could not complete the operation: {exc}")


if __name__ == "__main__":
    main()
