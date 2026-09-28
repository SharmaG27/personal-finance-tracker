import csv

import sys

from src.models import Transaction






class CSVParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):

        transactions = []

        try:
            with open(self.file_path, "r", encoding = "utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    transaction = Transaction(
                        row["date"],
                        row["description"],
                        row["amount"],
                        row["category"],
                        row["transaction_type"]
                    )

                    transactions.append(transaction)



        except FileNotFoundError:
            print(f"File not found at {self.file_path}. Exiting program.")

            sys.exit(1)

        return transactions



