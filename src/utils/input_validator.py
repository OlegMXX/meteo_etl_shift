from datetime import datetime


def input_validator(date_from: str, date_to: str):
    try:
        start = datetime.strptime(date_from, "%Y-%m-%d")
        end = datetime.strptime(date_to, "%Y-%m-%d")

        if start > end:
            raise ValueError("Error: Start date must be earlier than or equal to the end date.")
        if start < datetime.strptime("2025-05-01", "%Y-%m-%d"):
            raise ValueError("Error: The earliest available date for data is 2025-05-01")

        else:
            return True

    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD.")