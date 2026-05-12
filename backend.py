from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# ✅ Create Database & Table
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()

# ✅ Add Expense
@app.route('/add', methods=['POST'])
def add_expense():
    data = request.json

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
        (data['date'], data['category'], data['amount'], data['description'])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Expense Added Successfully"})

# ✅ Get Expenses (IMPORTANT FIX HERE)
@app.route('/expenses', methods=['GET'])
def get_expenses():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()

    # Convert rows → JSON objects
    expenses = []
    for row in rows:
        expenses.append({
            "id": row[0],
            "date": row[1],
            "category": row[2],
            "amount": row[3],
            "description": row[4]
        })

    return jsonify(expenses)

# ✅ Delete Expense (BONUS FEATURE 🔥)
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_expense(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id=?", (id,))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Deleted Successfully"})

# ✅ Run Server
if __name__ == '__main__':
    app.run(debug=True)

# from flask_cors import CORS
# CORS(app)
# import sqlite3

# app = Flask(__name__)

# # Create DB
# def init_db():
#     conn = sqlite3.connect("database.db")
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS expenses (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             date TEXT,
#             category TEXT,
#             amount REAL,
#             description TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# init_db()

# # Add expense
# @app.route('/add', methods=['POST'])
# def add_expense():
#     data = request.json

#     conn = sqlite3.connect("database.db")
#     c = conn.cursor()

#     c.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
#               (data['date'], data['category'], data['amount'], data['description']))

#     conn.commit()
#     conn.close()

#     return jsonify({"message": "Expense added"})

# # Get all expenses
# @app.route('/expenses', methods=['GET'])
# def get_expenses():
#     conn = sqlite3.connect("database.db")
#     c = conn.cursor()

#     c.execute("SELECT * FROM expenses")
#     rows = c.fetchall()

#     conn.close()

#     return jsonify(rows)

# if __name__ == '__main__':
#     app.run(debug=True)