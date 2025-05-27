from db import get_db_connection

def generate_monthly_report(user_id, month, year):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT type, SUM(amount) FROM transactions
        WHERE user_id = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
        GROUP BY type
    """, (user_id, f"{int(month):02d}", str(year)))
    data = cursor.fetchall()
    conn.close()

    income = sum(row[1] for row in data if row[0] == 'income')
    expense = sum(row[1] for row in data if row[0] == 'expense')
    savings = income - expense

    print(f"\n📅 Monthly Report for {month}/{year}")
    print(f"Total Income: ₹{income}")
    print(f"Total Expenses: ₹{expense}")
    print(f"Savings: ₹{savings}")

def generate_yearly_report(user_id, year):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT type, SUM(amount) FROM transactions
        WHERE user_id = ? AND strftime('%Y', date) = ?
        GROUP BY type
    """, (user_id, str(year)))
    data = cursor.fetchall()
    conn.close()

    income = sum(row[1] for row in data if row[0] == 'income')
    expense = sum(row[1] for row in data if row[0] == 'expense')
    savings = income - expense

    print(f"\n📅 Yearly Report for {year}")
    print(f"Total Income: ₹{income}")
    print(f"Total Expenses: ₹{expense}")
    print(f"Savings: ₹{savings}")
