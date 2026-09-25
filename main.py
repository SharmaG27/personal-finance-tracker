from src.parsers import CSVParser
from src.models import Account

parser = CSVParser("data/sample.csv")
transactions = parser.parse()

account = Account("Main Checking")

for transaction in transactions:
    account.add_transaction(transaction)


print(f"Total Income: £{account.total_income():.2f}")
print(f"Total Expenses: £{account.total_expenses():.2f}")
print(f"Net Balance: £{account.net_balance():.2f}")