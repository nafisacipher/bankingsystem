# customer.py

class Customer:
    #it represents a bank customer.
    #it stores the customer's name,id,a/c no and balance

    def set_customer(self, customername, customerid, account):
        """Initialize the customer manually."""
        self.customername = customername
        self.customerid = customerid
        self.account = account  # it links to the account object

    def show_details(self):
        #Display customer details and account balance.
        print("Customer Name: " + self.customername)   #prints customer's name
        print("Customer ID: " + self.customerid)  # prints customer's ID
        print("Account Number: " + str(self.account.accountnumber))  #prints A/C
        print("Balance: ₹" + str(self.account.get_balance()))  #prints the balance of the account
