# import streamlit as st
# import pandas as pd

# st.title("💰 Expense Tracker Dashboard")

# # Input fields
# date = st.date_input("Select Date")
# category = st.text_input("Enter Category")
# amount = st.number_input("Enter Amount")
# description = st.text_input("Description")

# # Add Expense Button
# if st.button("Add Expense"):
#     new_data = {
#         "date": date,
#         "category": category,
#         "amount": amount,
#         "description": description.replace(",", " ")
#     }

#     df = pd.DataFrame([new_data])
#     df.to_csv("expenses.csv", mode='a', header=False, index=False)

#     st.success("✅ Expense Added!")

# # Show Data
# st.subheader("📊 Expense Data")

# try:
#     df = pd.read_csv("expenses.csv")
#     st.dataframe(df)

#     # Total spending
#     total = df["amount"].sum()
#     st.write(f"### Total Spending: ₹{total}")

#     # Category-wise
#     st.subheader("Category-wise Spending")
#     st.bar_chart(df.groupby("category")["amount"].sum())

# except Exception as e:
#     st.error(f"Error: {e}")