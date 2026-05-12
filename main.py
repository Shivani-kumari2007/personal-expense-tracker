import pandas as pd

# 🔹 Function to add expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/etc): ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")
        return
    
    # 🔥 Prevent comma issues in CSV
    description = input("Enter description: ").replace(",", " ")

    new_data = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    df = pd.DataFrame([new_data])

    # Append to CSV safely
    df.to_csv("expenses.csv", mode='a', header=False, index=False)

    print("✅ Expense added successfully!")


# 🔹 Function to view summary
def view_summary():
    try:
        # 🔥 Skip bad lines instead of crashing
        df = pd.read_csv("expenses.csv", on_bad_lines='skip')

        if df.empty:
            print("⚠️ No data available!")
            return

        print("\n📊 Expense Summary")

        # Total spending
        total = df["amount"].sum()
        print(f"Total Spending: ₹{total}")

        # Category-wise spending
        category_sum = df.groupby("category")["amount"].sum()
        print("\nSpending by Category:")
        print(category_sum)

        # Highest expense category
        highest = category_sum.idxmax()
        print(f"\nHighest Spending Category: {highest}")

    except FileNotFoundError:
        print("❌ No expense data found!")
    except Exception as e:
        print(f"❌ Error: {e}")


# 🔹 Main menu
def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

# 🔥 Run program
main()