from datetime import datetime


class Transaction:
    def __init__(self, date, description, amount, category, transaction_type):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.description = description
        self.amount = float(amount)
        self.category = category
        self.transaction_type = transaction_type.lower()

    def __repr__(self):
        date_formatted = self.date.strftime("%Y-%m-%d")
        return f"Transaction ({date_formatted} | {self.description} | {self.amount} | {self.transaction_type})"

    def is_expense(self):
        return self.transaction_type == "expense"





class Account:
    def __init__(self, account_name):
        self.account_name = account_name
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def total_income(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.transaction_type == "income")

    def net_balance(self):
        return self.total_income() - self.total_expenses()

    def total_expenses(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.is_expense())