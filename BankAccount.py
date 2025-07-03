class BankAccount:
    ## Global Attribute
    customerBank = "Wells Fargo"

    ## Initializing Attributes for BankAccount Class, Created Private Members
    def __init__(self, name, balance=0.0):
        self.__customerName = name
        self.__customerBalance = balance
        self.__customerMinBalance = 50.0

    ## Getter Methods to Access Private Memebers
    def getCustomerName(self):
        return self.__customerName

    def getCustomerBalance(self):
        return self.__customerBalance

    def getCustomerMinBalance(self):
        return self.__customerMinBalance

    ##Assignments Function Requirements
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit Failed: PLEASE DEPOSIT VALID VALUE.")
        else:
            self.__customerBalance += amount
            print(f"Deposit Successful:\n    NEW BALANCE {self.__customerBalance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw Failed: PLEASE ENTER VALID VALUE.")
        elif self.__customerBalance - amount < self.__customerMinBalance:
            print(f"Withdraw Failed:\n    CANNOT WITHDRAW MINIMUM BALANCE: {self.__customerMinBalance}.")
        else:
            self.__customerBalance -= amount
            print(f"Withdraw Successful: New Balance is {self.__customerBalance}")

    def print_customer_information(self):
        print("BankAccount Information")
        print("------------------------------------------")
        print(f"Bank Title: {BankAccount.customerBank}")
        print(f"Customer Name: {self.__customerName}")
        print(f"Account Balance: {self.__customerBalance}")
        print(f"Minimum Required Balance: {self.__customerMinBalance}")

    def __str__(self):
        return (f"BankAccount Information\n"
                f"------------------------------------------\n"
                f"Bank Title: {BankAccount.customerBank}\n"
                f"Customer Name: {self.__customerName}\n"
                f"Account Balance: {self.__customerBalance}\n"
                f"Minimum Required Balance: {self.__customerMinBalance}")
