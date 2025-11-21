# transaction.py

class Transaction:
    
    #Handles transferring money between accounts and storing transaction history.
    

    # its a list to store transaction history
    history = []

    def transfer(self, fromaccount, toaccount, transactionamount):
        #it transfers money from one account to another
        if transactionamount <= 0:
            print("Transfer failed.The amount must be greater than 0.")
            return

        if fromaccount.get_balance() < transactionamount:
            print("Transfer failed. There is an insufficient balance in the source account.")
            return

        # it withdraws from the source account
        fromaccount.withdraw(transactionamount)
        # it deposits into the destination account
        toaccount.deposit(transactionamount)

        # it saves the record in transaction history
        Transaction.history.append(
            "Transferred ₹" + str(transactionamount) +
            " from Account " + str(fromaccount.accountnumber) +
            " to Account " + str(toaccount.accountnumber)
        )
        print("Transfer of amount " + str(transactionamount) + " is successful")

    def show_history(self):
        #Displays all past transactions.
        print("\n--- Transaction History ---")
        if not Transaction.history:
            print("there has been no transactions yet")
        else:
            for record in Transaction.history:
                print(record)
