import sqlite3
import shutil
import os

def backup_database():
    if os.path.exists("finance_app.db"):
        shutil.copy("finance_app.db", "finance_app_backup.db")
        print("✅ Backup created as 'finance_app_backup.db'.")
    else:
        print("❌ No database found to backup.")

def restore_database():
    if os.path.exists("finance_app_backup.db"):
        shutil.copy("finance_app_backup.db", "finance_app.db")
        print("✅ Database restored from 'finance_app_backup.db'.")
    else:
        print("❌ No backup file found to restore.")
