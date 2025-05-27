from db import get_db_connection

def set_budget(user_id):
    category = input("Enter category: ").strip()
    limit = float(input("Enter budget limit: "))
    month = input("Enter month (MM): ").strip()
    year = input("Enter year (YYYY): ").strip()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO budgets (user_id, category, "limit", month, year)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, category, limit, month, year))
    conn.commit()
    conn.close()
    print("Budget set successfully.")

def check_budget(user_id, category, amount, date):
    conn = get_db_connection()
    cursor = conn.cursor()
    month = date[5:7]
    year = date[0:4]
    cursor.execute("""
        SELECT "limit" FROM budgets
        WHERE user_id = ? AND category = ? AND month = ? AND year = ?
    """, (user_id, category, month, year))
    result = cursor.fetchone()
    if result:
        limit = result[0]
        cursor.execute("""
            SELECT SUM(amount) FROM transactions
            WHERE user_id = ? AND category = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
        """, (user_id, category, month, year))
        total = cursor.fetchone()[0] or 0
        if total + amount > limit:
            print(f"⚠️ Warning: This transaction exceeds your budget for {category} in {month}/{year}.")
    conn.close()
