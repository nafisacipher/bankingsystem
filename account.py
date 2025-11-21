# This module is account.py

class Account:    # This module defines the Account class to manage a bank account


    def set_account(self, accountnumber, startingbalance=0):
        #it initializes the account manually
        self.accountnumber = accountnumber
        self.balanceamount = startingbalance  # it stores the balance as an object attribute

    def deposit(self, transactionamount):
        # it adds money to that account
        if transactionamount > 0:
            self.balanceamount += transactionamount
            print("₹" + str(transactionamount) + " deposited successfully. Your new balance is: ₹" + str(self.balanceamount))
        else:
            print("Deposit failed. Amount must be greater than 0.")

    def withdraw(self, transactionamount):
        # it Withdraws the money from the account
        if transactionamount <= 0:
            print("Withdrawal failed! Amount must be greater than 0.")
        elif transactionamount > self.balanceamount:
            print("Withdrawal failed! Insufficient balance.")
        else:
            self.balanceamount -= transactionamount
            print("₹" + str(transactionamount) + " withdrawn successfully! Remaining balance: ₹" + str(self.balanceamount))

    def get_balance(self):
        #Return the current balance of the account
        return self.balanceamount
