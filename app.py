import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Expense Tracker", layout="wide")

st.title("💰 Expense Tracker Dashboard")

# ------------------ ADD EXPENSE ------------------
st.subheader("➕ Add New Expense")

date = st.date_input("Select Date")
category = st.text_input("Enter Category")
amount = st.number_input("Enter Amount", min_value=0.0)
description = st.text_input("Description")

if st.button("Add Expense"):
    new_data = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description.replace(",", " ")
    }

    df_new = pd.DataFrame([new_data])

    file_exists = os.path.isfile("expenses.csv")

    df_new.to_csv("expenses.csv", mode='a', header=not file_exists, index=False)

    st.success("✅ Expense Added!")

# ------------------ LOAD DATA ------------------
st.subheader("📊 Expense Data")

try:
    df = pd.read_csv("expenses.csv")

    # Convert date column
    df["date"] = pd.to_datetime(df["date"], errors='coerce')

    # Drop invalid rows
    df = df.dropna()

    # ------------------ SIDEBAR FILTER ------------------
    st.sidebar.header("📅 Filter Data")

    df["month"] = df["date"].dt.to_period("M").astype(str)

    selected_month = st.sidebar.selectbox(
        "Select Month",
        options=df["month"].unique()
    )

    filtered_df = df[df["month"] == selected_month]

    # ------------------ SHOW DATA ------------------
    st.subheader(f"📅 Data for {selected_month}")
    st.dataframe(filtered_df)

    # ------------------ TOTAL SPENDING ------------------
    total = filtered_df["amount"].sum()
    st.write(f"### 💸 Total Spending: ₹{int(total)}")

    # ------------------ BAR CHART ------------------
    st.subheader("📊 Category-wise Spending")
    bar_data = filtered_df.groupby("category")["amount"].sum()
    st.bar_chart(bar_data)

    # ------------------ PIE CHART ------------------
    st.subheader("🥧 Category Distribution")

    if len(bar_data) > 0:
        st.pyplot(bar_data.plot.pie(autopct='%1.1f%%').figure)

    # ------------------ PREDICTION ------------------
    st.subheader("📈 Spending Prediction")

    df_sorted = df.sort_values("date")
    df_sorted["days"] = (df_sorted["date"] - df_sorted["date"].min()).dt.days

    if len(df_sorted) > 1:
        x = df_sorted["days"]
        y = df_sorted["amount"]

        coeffs = np.polyfit(x, y, 1)
        future_day = x.max() + 7

        prediction = np.polyval(coeffs, future_day)

        st.info(f"💡 Estimated spending in next 7 days: ₹{int(prediction)}")
    else:
        st.warning("Not enough data for prediction")

except Exception as e:
    st.error(f"Error: {e}")
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