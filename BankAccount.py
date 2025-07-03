class BankAccount:
    ## Global Attribute
    _customerBank = "Wells Fargo"

    ## Initializing Attributes for BankAccount Class, Created Private Members
    def __init__(self, name, balance=0.0):
        self._customerName = name
        self._customerBalance = balance
        self._customerMinBalance = 50.0

    ## Getter Methods to Access Protected Members
    def getCustomerBank(self):
        return self._customerBank
    def getCustomerName(self):
        return self._customerName

    def getCustomerBalance(self):
        return self._customerBalance

    def getCustomerMinBalance(self):
        return self._customerMinBalance

    ##Assignments Function Requirements
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit Failed: PLEASE DEPOSIT VALID VALUE.")
        else:
            self._customerBalance += amount
            print(f"Deposit Successful:\n    NEW BALANCE {self._customerBalance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw Failed: PLEASE ENTER VALID VALUE.")
        elif self._customerBalance - amount < self._customerMinBalance:
            print(f"Withdraw Failed:\n    CANNOT WITHDRAW MINIMUM BALANCE: {self._customerMinBalance}.")
        else:
            self._customerBalance -= amount
            print(f"Withdraw Successful: New Balance is {self._customerBalance}")

    def print_customer_information(self):
        print("BankAccount Information")
        print("------------------------------------------")
        print(f"Bank Title: {BankAccount.customerBank}")
        print(f"Customer Name: {self._customerName}")
        print(f"Account Balance: {self._customerBalance}")
        print(f"Minimum Required Balance: {self._customerMinBalance}")

    def __str__(self):
        return (f"BankAccount Information\n"
                f"------------------------------------------\n"
                f"Bank Title: {BankAccount.customerBank}\n"
                f"Customer Name: {self._customerName}\n"
                f"Account Balance: {self._customerBalance}\n"
                f"Minimum Required Balance: {self._customerMinBalance}")
