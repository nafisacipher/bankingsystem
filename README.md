# Mini Banking System

## Project Overview
The **Mini Banking System** is a console-based Python application designed to simulate a basic banking environment.  
It allows users to create bank accounts, deposit and withdraw money, transfer funds between accounts, and view reports and transaction histories.  

The project applies object-oriented programming concepts such as classes, methods, and modular design. It also demonstrates proper version control and project organization.

---

## Features
The system provides the following major features:

1. **Account Management**
   - Create new accounts with unique account numbers.
   - Track account balances.

2. **Customer Management**
   - Store customer details such as name and ID.
   - Link customers to their accounts.

3. **Transactions**
   - Deposit money into accounts.
   - Withdraw money from accounts with balance checks.
   - Transfer money between accounts with transaction history tracking.

4. **Reports**
   - Display all accounts with their balances.
   - Show transaction history for all transfers.

---

## Technologies & Tools Used
- **Programming Language:** Python 3.13  
- **IDE:** VS Code  
- **Version Control:** Git & GitHub  
- **Modules/Packages:** Standard Python libraries only (no external dependencies)  

---

## Project Structure


##​‍​‌‍​‍‌​‍​‌‍​‍‌ Functional Requirements 

- Ability to open accounts and have customer information saved. 

- Money should be put in and taken out with proper validations. 

- Money should be moved from one account to another in a secure way. 

- It should be possible to view all accounts with their balances. 

- The bank should keep track of the transaction history. 

--- 

## Non-Functional Requirements 

- **Usability:** User-friendly console interface with menu-driven options. 

- **Reliability:** Each transaction has to be validated and verified. 

- **Performance:** Operations should be completed fast with very little processing delay. 

- **Maintainability:** The program should be designed in a modular way with separate classes for account, customer, transaction, and reporting. 


banking-system/ 

──​‍​‌‍​‍main.py # The main module to execute the program and get inputs from the user 

── account.py # Contains the definition of Account class for the account management 

── customer.py # Contains the definition of the Customer class for customer-related data 

── transaction.py # Contains the definition of the Transaction class for money transfers 

── report.py # Contains the definition of Report class for generating reports 

── statement.md # Project statement including problem statement and scope 

── README.md # Project summary and user ​‍​‌‍​‍‌​‍​‌‍​‍‌guide 



How to Use / Testing Instructions

Main Menu Options

1. Create Account: Enter a unique account number and customer name.

2. Deposit Money: Enter account number and deposit amount. Check balance updates.

3. Withdraw Money: Enter account number and withdrawal amount. Validate sufficient balance.

4. Transfer Money: Enter source and destination account numbers, then transfer amount.

5. Show All Accounts: Displays account numbers and current balances.

6. Show Transaction History: Lists all money transfers between accounts.

7. Exit: Exit the program.

Testing

-Test deposits, withdrawals, and transfers for multiple accounts.
-Ensure transaction history updates after every transfer.
-Check balance updates are accurate after each operation.
