from db import create_tables
from auth import register, login
from finance import finance_menu
from backup import backup_database, restore_database

def main():
    create_tables()
    while True:
        print("\n Personal Finance Management System ")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("4. Backup Data")
        print("5. Restore Data")

        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            user_id = login()
            if user_id:
                finance_menu(user_id)
        elif choice == '3':
            print("👋 Goodbye!")
            break
        elif choice == '4':
            backup_database()
        elif choice == '5':
            restore_database()
        else:
            print("❗ Invalid option")

if __name__ == "__main__":
    main()
