import pandas as pd

# 🔹 Function to add expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/etc): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    new_data = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    df = pd.DataFrame([new_data])

    df.to_csv("expenses.csv", mode='a', header=False, index=False)

    print("✅ Expense added successfully!")


def main():
    while True:
        print("\n1. Add Expense")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


main()