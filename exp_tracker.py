import json
from datetime import datetime

# File name
FILE_NAME = "expenses.json"


# Load expenses from file
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):
    amount = float(input("Enter Amount: ₹"))
    category = input("Enter Category (Food, Transport, Entertainment, etc.): ")

    date = input("Enter Date (YYYY-MM-DD) or press Enter for today: ")

    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense Added Successfully!\n")


# View all expenses
def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found.\n")
        return

    print("\n----- Expense Records -----")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{expense['amount']} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )

    print()


# View summary
def view_summary(expenses):
    if len(expenses) == 0:
        print("No expenses available.\n")
        return

    total_spending = 0
    category_totals = {}

    for expense in expenses:
        total_spending += expense["amount"]

        category = expense["category"]

        if category in category_totals:
            category_totals[category] += expense["amount"]
        else:
            category_totals[category] = expense["amount"]

    print("\n----- Expense Summary -----")

    print(f"Total Spending: ₹{total_spending}")

    print("\nCategory Wise Spending:")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount}")

    print()


# Main Program
def main():
    expenses = load_expenses()

    print("===== Personal Expense Tracker =====")

    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            view_summary(expenses)

        elif choice == "4":
            print("Thank You for Using Expense Tracker!")
            break

        else:
            print("Invalid Choice! Please Try Again.")


main()