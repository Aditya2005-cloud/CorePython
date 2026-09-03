from datetime import datetime


def validate_positive_number(value):
    try:
        value = float(value)
    except (ValueError, TypeError):
        raise ValueError("Value must be a number.")

    if value <= 0:
        raise ValueError("Value must be greater than zero.")

    return value


def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be YYYY-MM-DD.")

    return date_string


def validate_month(month):
    month = int(month)

    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12.")

    return month


def validate_year(year):
    year = int(year)

    if year < 2000:
        raise ValueError("Invalid year.")

    return year


def validate_non_empty(value, field_name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")

    return value.strip()
