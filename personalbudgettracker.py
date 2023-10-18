import csv
import os

class BudgetTracker:
    def __init__(self, budget_file="budget.csv"):
        self.budget_file = budget_file
        self.categories = set()
        self.budget = {}
        self.expenses = []

        self.load_budget_data()

    def load_budget_data(self):
        if os.path.exists(self.budget_file):
            with open(self.budget_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    category = row['Category']
                    amount = float(row['Amount'])
                    self.budget[category] = amount
                    self.categories.add(category)

    def save_budget_data(self):
        with open(self.budget_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Category', 'Amount'])
            for category, amount in self.budget.items():
                writer.writerow([category, amount])

    def display_budget(self):
        print("\nBudget Categories:")
        for category, amount in self.budget.items():
            print(f"{category}: ${amount:.2f}")

    def add_category(self, category, amount):
        self.budget[category] = amount
        self.categories.add(category)
        self.save_budget_data()

    def record_income(self, category, amount):
        if category in self.budget:
            self.budget[category] += amount
            self.save_budget_data()
            print(f"Income of ${amount:.2f} recorded in '{category}' category.")
        else:
            print(f"Category '{category}' not found in the budget.")

    def record_expense(self, category, amount):
        if category in self.budget:
            if self.budget[category] >= amount:
                self.budget[category] -= amount
                self.expenses.append((category, amount))
                self.save_budget_data()
                print(f"Expense of ${amount:.2f} recorded in '{category}' category.")
            else:
                print(f"Insufficient funds in '{category}' category.")
        else:
            print(f"Category '{category}' not found in the budget.")

    def show_expense_analysis(self):
        print("\nExpense Analysis:")
        total_expense = sum(amount for _, amount in self.expenses)
        print(f"Total Expenses: ${total_expense:.2f}")
        for category, amount in self.budget.items():
            print(f"Remaining Budget in '{category}': ${amount:.2f}")

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\nOptions:")
        print("1. Display Budget")
        print("2. Add Category")
        print("3. Record Income")
        print("4. Record Expense")
        print("5. Show Expense Analysis")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            budget_tracker.display_budget()
        elif choice == "2":
            category = input("Enter category name: ")
            amount = float(input("Enter budget amount: "))
            budget_tracker.add_category(category, amount)
        elif choice == "3":
            category = input("Enter category for income: ")
            amount = float(input("Enter income amount: "))
            budget_tracker.record_income(category, amount)
        elif choice == "4":
            category = input("Enter category for expense: ")
            amount = float(input("Enter expense amount: "))
            budget_tracker.record_expense(category, amount)
        elif choice == "5":
            budget_tracker.show_expense_analysis()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
