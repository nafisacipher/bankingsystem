# main.py is the module here
# Mini Banking System 

from account import Account      # this imports Account class to create and manage accounts
from customer import Customer    # this imports Customer class to store customer information
from transaction import Transaction  # this imports Transaction class to handle money transfers
from report import Report        # this imports Report class to show all accounts

# these are the lists to keep track of all accounts and customers
allaccounts = []   # it keeps the track of every account created in the system
allcustomers = []  # it keeps the track of every customer in the system

# Main menu function to interact with the user and to do the task accordingly 
def mainmenu():
    while True:
        print("\n=== Mini Banking System ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Show All Accounts")
        print("6. Show Transaction History")
        print("7. Exit")

        choice = input("Enter your choice: ")  # Asking the user to choose an option

        if choice == "1":
            createaccount()    # its an call function to create new account
        elif choice == "2":
            depositmoney()     # its an call function to deposit money
        elif choice == "3":
            withdrawmoney()    # its an call function to withdraw money
        elif choice == "4":
            transfermoney()    # its an call function to transfer money
        elif choice == "5":
            rep = Report()     # it creates a Report object
            rep.show_accounts(allaccounts)   # this helps to show all accounts
        elif choice == "6":
            trans = Transaction()             # Creates a Transaction object
            trans.show_history()              # it shows the entire transaction history
        elif choice == "7":
            print("Thank you for using Mini Banking System.")  # Exit message once they have used the features
            break
        else:
            print("Invalid choice. Please try again.")  # prints when the user gives an invalid input

# Function to create new account and customer
def createaccount():
    accnumber = input("Enter new account number: ")   # we ask the user for account number
    customername = input("Enter customer name: ")     # we ask the user for customer name

    newaccount = Account()         # we create an Account object
    newaccount.set_account(accnumber, 0)  # we initialize it with 0 balance
    allaccounts.append(newaccount)        # it adds to accounts list

    newcustomer = Customer()       # Creates an object called Customer object
    newcustomer.set_customer(customername, "C" + str(accnumber), newaccount)  # Links the given account
    allcustomers.append(newcustomer)     # it adds to customers list

    print("Account created successfully for " + customername )  # giving confirmation that account has been created

# a function to deposit money into the account
def depositmoney():
    accnumber = input("Enter account number: ")   # asks the user for account number
    account = findaccount(accnumber)             # it finds the account object
    if account:
        amount = float(input("Enter amount to deposit: "))  # it asks for the deposit amount
        account.deposit(amount)                            #it calls the deposit method
    else:
        print("Account not found")                        # prints the given statement if entered account is not found in the system

# a function to withdraw money from an account
def withdrawmoney():
    accnumber = input("Enter account number: ")   # asks the user for account number
    account = findaccount(accnumber)             # it finds the account object
    if account:
        amount = float(input("Enter amount to withdraw: "))  # it asks for withdrawal amount
        account.withdraw(amount)                            # it calls the withdraw method
    else:
        print("Account not found!")                        #prints the given statement if entered account is not found in the system


# a function to transfer money between accounts
def transfermoney():
    fromacc = input("Enter FROM account number: ")   # asks user for source account
    toacc = input("Enter TO account number: ")       # asks user for destination account

    fromaccount = findaccount(fromacc)    # it finds the source account object
    toaccount = findaccount(toacc)        # it finds the destination account object

    if fromaccount and toaccount:         # condition incase both accounts exist
        amount = float(input("Enter amount to transfer: "))  # Asks the amount to be transferred
        trans = Transaction()             # it creates a Transaction object
        trans.transfer(fromaccount, toaccount, amount)  # Execute the transfer from one account to the other
    else:
        print("One or both accounts not found!")  # prints the given statement if the accounts are not found in the system


# its an helper function to find an account by its number
def findaccount(accnumber):
    for acc in allaccounts:            # this loops through all accounts to find the specific account
        if acc.accountnumber == accnumber:  # this matches the account number to the account number which was found
            return acc                     # it returns the account object
    return None                            # it returns None if the account is not found

# the program starts here
if __name__ == "__main__":
    mainmenu()   # it calls the main menu function
