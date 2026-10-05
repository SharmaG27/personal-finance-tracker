from src.parsers import CSVParser
from src.models import Account
from src.visualisations import plot_category_breakdown

parser = CSVParser("data/sample.csv")


transactions = parser.parse()

account = Account("Main Checking")

for transaction in transactions:
    account.add_transaction(transaction)


print(f"Total Income: £{account.total_income():.2f}")
print(f"Total Expenses: £{account.total_expenses():.2f}")
print(f"Net Balance: £{account.net_balance():.2f}")
print()

breakdown = account.category_breakdown()

breakdown_sorted = sorted(breakdown.items(), key = lambda item: item[1], reverse = True)


print("Breakdown of expenses per category (descending):")

print()

for category, amount in breakdown_sorted:
    print(f"{category}: £{amount:.2f}")

plot_category_breakdown(account)


