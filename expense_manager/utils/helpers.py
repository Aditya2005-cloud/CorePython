from datetime import datetime


def generate_id(objects, attribute):
    if not objects:
        return 1

    return max(getattr(obj, attribute) for obj in objects) + 1


def format_currency(amount):
    return f"₹{amount:,.2f}"


def current_date():
    return datetime.now().strftime("%Y-%m-%d")


def get_month_name(month):
    return datetime(2000, month, 1).strftime("%B")
