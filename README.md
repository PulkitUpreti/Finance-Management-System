# Finance-Management-System
Personal Finance Management System is a command-line Python application that helps users track income, expenses, and budgets efficiently. It supports user registration, category-wise tracking, financial reports, and SQLite-based data storage. 

Personal Finance Management Application – User Manual
Command-Line Based  Personal Finance Management Application

Author  :  Pulkit Upreti
Date of Submission  :  May 28, 2025

Table of Contents
1.	 Introduction
2.   System Requirements
2.	 Installation Instructions
3.	 Folder Structure
4.	 Getting Started
5.	 Using the Finance Menu
6.	 Backup and Restore
7.	 Sample Use Case
8.	 Error Handling / Troubleshooting
9.	 FAQs
10.	 Future Enhancements
11.	 Conclusion

Introduction
This application allows users to manage their income and expenses, set budgets, and generate financial reports using a simple command-line interface.

System Requirements
- Operating System: Windows 10/11, macOS, Linux
- Python 3.7 or above
- SQLite3 (included with Python)
- Command Prompt / Terminal


Installation Instructions
1. Download or clone the project folder `Personal_Finance_System` to your Desktop.
2. Ensure Python is installed. Download from https://www.python.org/downloads/
3. Open Command Prompt and navigate to the project folder:
   cd Desktop\Personal_Finance_System
4. Run the application:
   python main.py

Folder Structure
Personal_Finance_System/
├── main.py           # Launches the application
├── auth.py           # Handles login and registration
├── db.py             # Manages database connection
├── finance.py        # Core finance features (add/view/update/delete)
├── report.py         # Financial reports
├── budget.py         # Budget setting and notifications
├── backup.py         # Backup and restore features
└── finance_app.db    # SQLite database file (auto-created)

Getting Started
1. Run `main.py` to launch the app.
2. Choose option 1 to Register.
   - Username : Pulkit Upreti
   - Password : 123
3. After registration, login using option 2.
4. Use the finance menu to manage your transactions.
Using the Finance Menu

Finance Menu:
1. Add Transaction
2. View Transactions
3. Update Transaction
4. Delete Transaction
5. Logout
6. Generate Monthly Report
7. Generate Yearly Report
8. Set Budget

Backup and Restore
Use options 4 and 5 in the main menu:
- Backup Data : Saves `finance_app.db.backup`
- Restore Data : Restores from `.backup` file

Sample Use Case
1. Register with username : Pulkit Upreti, password : 123
2. Add income transaction : Type=income, Category=Salary, Amount=5000
3. Add expense transaction : Type=expense, Category=Food, Amount=1000
4. Set budget for Food = 2000
5. Generate Monthly Report

Error Handling / Troubleshooting
- NameError  :  Function not imported
- sqlite3.OperationalError  :   Quote SQL keywords like `limit`
- Command not recognized  :   Ensure proper `cd` and `python` usage
  
FAQs
- Where is my data stored? → In `finance_app.db`
- Can I reset my password? → Not currently supported
- Will this work offline? → Yes, it’s fully local

Future Enhancements
- Export reports to CSV
- Add a graphical user interface (GUI)- Cloud data syncConclusion
This command-line application helps users easily manage personal finances in a structured, local, and secure way.
