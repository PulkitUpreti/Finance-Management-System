import sqlite3
from db import get_db_connection
from utils import hash_password, verify_password

def register():
    conn = get_db_connection()
    cursor = conn.cursor()

    username = input("Choose a username: ").strip()
    password = input("Choose a password: ").strip()

    hashed = hash_password(password)

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
        print("✅ Registration successful!")
    except sqlite3.IntegrityError:
        print("❌ Username already exists.")
    finally:
        conn.close()

def login():
    conn = get_db_connection()
    cursor = conn.cursor()

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    conn.close()

    if result and verify_password(result[1], password):
        print("✅ Login successful!")
        return result[0]  # Return user_id
    else:
        print("❌ Invalid credentials.")
        return None
