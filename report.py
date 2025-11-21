# report.py

class Report:
    # this generates the reports for all bank accounts.
    

    def show_accounts(self, accounts):
        #it displays all the accounts and their balances.
        print("\n--- All Accounts ---")
        if not accounts:
            print("No accounts available.")
        else:
            for account in accounts:
                print("Account Number: " + str(account.accountnumber) +
                      ", Balance: ₹" + str(account.get_balance()))
