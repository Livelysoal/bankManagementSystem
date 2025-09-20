# 🏦 Laximi Chit Fund Bank

A **console-based Python banking system** for creating accounts, managing deposits and withdrawals, viewing account details, and updating user information. All data is stored persistently using JSON.

---

## 🌟 Features

- ✅ Create new bank accounts with validations  
- ✅ Deposit and withdraw money securely  
- ✅ View account details (secured with PIN)  
- ✅ Update email, phone number, or PIN  
- ✅ Persistent data storage using `JSON`  
- ✅ User-friendly console interface  

---

## 📋 Validations

- Age must be **18 or above**  
- Email must contain `@` and end with `.com`  
- Phone number must be **10 digits**  
- PIN must be **4 digits**  
- Deposits and withdrawals must be **positive amounts**  
- Withdrawals cannot exceed account balance  
- PIN verification required for sensitive operations  

```
***********************************************
     Welcome to Laximi Chit Fund Bank..😁😊
***********************************************
1. Create a new bank account
2. Deposit money in account
3. Withdraw money from account
4. View account details
5. Update account details
6. Exit
Enter your choice from the above list:

```


## 🛠 Requirements

-Python 3

-Built-in libraries: json, random, pathlib


## ⚙️ How It Works

- User accounts are stored as dictionaries in a list
- All data is saved in database.json for persistence
- Instance methods handle operations: create, deposit, withdraw, view, update
- Class method __update writes changes to the JSON file
- Input validation ensures safe and correct transactions

## 👤 Author

-ayush 

-GitHub: https://github.com/Livelysoal




