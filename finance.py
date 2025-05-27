import sqlite3
from db import get_db_connection
from reports import generate_monthly_report, generate_yearly_report
from budget import check_budget
from datetime import datetime
from budget import set_budget



def add_transaction(user_id):
    type_ = input("Type (Income/Expense): ").strip().lower()
    category = input("Category (e.g., Food, Salary): ").strip()
    amount = float(input("Amount: "))
    date = datetime.now().strftime("%Y-%m-%d")
    check_budget(user_id, category, amount, date)
    description = input("Description (optional): ")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (user_id, type, category, amount, description)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, type_, category, amount, description))
    conn.commit()
    conn.close()
    print("Transaction added.")

def view_transactions(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, type, category, amount, date, description FROM transactions WHERE user_id = ?", (user_id,))
    transactions = cursor.fetchall()
    conn.close()

    print("\n📋 Your Transactions :")
    for t in transactions:
        print(f"[{t[0]}] {t[1].upper()} | {t[2]} | ₹{t[3]} | {t[4]} | {t[5]}")

def update_transaction(user_id):
    view_transactions(user_id)
    trans_id = input("Enter transaction ID to update: ")
    new_amount = float(input("New amount : "))
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE transactions SET amount = ? WHERE id = ? AND user_id = ?", (new_amount, trans_id, user_id))
    conn.commit()
    conn.close()
    print("Transaction updated.")

def delete_transaction(user_id):
    view_transactions(user_id)
    trans_id = input("Enter transaction ID to delete : ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ? AND user_id = ?", (trans_id, user_id))
    conn.commit()
    conn.close()
    print("Transaction deleted.")

def finance_menu(user_id):
    while True:
        print("\n💼 Finance Menu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Logout")
        print("6. Generate Monthly Report")
        print("7. Generate Yearly Report")
        print("8. Set Budget")
        choice = input("Select an option : ")

        if choice == '1':
            add_transaction(user_id)

        elif choice == '2':
            view_transactions(user_id)

        elif choice == '3':
            update_transaction(user_id)

        elif choice == '4':
            delete_transaction(user_id)

        elif choice == '5':
            print("Logging out...")
            break

        elif choice == '6':
            month = input("Enter month (MM): ")
            year = input("Enter year (YYYY): ")
            generate_monthly_report(user_id, month, year)

        elif choice == '7':
            year = input("Enter year (YYYY): ")
            generate_yearly_report(user_id, year)

        elif choice == '8':
            set_budget(user_id)

        else:
            print("⚠️ Invalid option.")
