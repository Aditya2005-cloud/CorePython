import csv
from pathlib import Path


class CSVStorage:
    def __init__(self, directory="reports"):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)

    def export_transactions(self, filename, transactions):
        path = self.directory / filename

        if not transactions:
            return

        fieldnames = [
            "transaction_id",
            "amount",
            "description",
            "category",
            "date",
            "transaction_type",
        ]

        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for transaction in transactions:
                writer.writerow(transaction.to_dict())
