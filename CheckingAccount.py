from BankAccount import BankAccount
import random

class CheckingAccount(BankAccount):
    ## Initializing Attributes for CheckingAccount SubClass w/Private Members
    def __init__(self, name, balance=0.0):
        super().__init__(name, balance)
        self.__routingNumber = random.randint(1000000000, 9999999999) # Unique Routing Number
        self.__accountNumber = random.randint(1000000000, 9999999999) # Unique Account Number
        self._transferLimit = 1500.50
        self._transferLimitExceeded = False
    ## Access to Private Members
    def getRoutingNumber(self):
        return self.__routingNumber

    def getAccountNumber(self):
        return self.__accountNumber

    ## Assignment Requirements: Added Checking Limit
    def depositLimit(self, amount):
        if amount > self._transferLimit:
            print(f"Deposit Failed:\n    ${amount} exceeds ${self._transferLimit:.2f} Daily Transfer Timit.")
            print("Please wait 24 hours to continue.")
            self._transferLimitExceeded = True
        else:
            self.deposit(amount)
            newTransferLimit = self._transferLimit + amount
            print(f"Transfer Limit: {self._transferLimit:.2f} => {newTransferLimit:.2f} ")

    def __str__(self):
        return (f"{self.getCustomerBank()} Checking Account Information: \n"
                f"------------------------------------------\n"
                f"Customer Name: {self._customerName}\n"
                f"Account Number: {self.__accountNumber}\n"
                f"Routing Number: {self.__routingNumber}\n"
                f"Current Balance: ${self._customerBalance:.2f}\n"
                f"Transfer Limit: {self._transferLimit:.2f}\n"
                f"Transfer Limit Exceeded: {self._transferLimitExceeded}")
