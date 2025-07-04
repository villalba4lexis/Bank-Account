from BankAccount import BankAccount
import random

class CheckingAccount(BankAccount):
    ## Initializing Attributes for CheckingAccount SubClass w/Private Members
    def __init__(self, name, balance=0.0):
        super().__init__(name, balance)
        self.__routingNumber = random.randint(1, 20)
        self.__accountNumber = random.randint(1, 10)
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
            print(f"Deposit Failed: Amount exceeds ${self._transferLimit:.2f} daily transfer limit.")
            print("Please wait 24 hours to continue.")
            self._transferLimitExceeded = True
        else:
            self.deposit(amount)

    def __str__(self):
        return (f"{self.customerBank} Checking Account Information: \n"
                f"------------------------------------------\n"
                f"Customer Name: {self.getCustomerName()}\n"
                f"Account Number: {self.__accountNumber}\n"
                f"Routing Number: {self.__routingNumber}\n"
                f"Current Balance: ${self.getCustomerBalance():.2f}\n"
                f"Transfer Limit: ${self._transferLimit:.2f}\n"
                f"Transfer Limit Exceeded: {self._transferLimitExceeded}")
