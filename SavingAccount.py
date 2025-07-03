from BankAccount import BankAccount
import random

class SavingAccount(BankAccount):
    ## Initializing Attributes for SavingAccount Sub-Class w/ Private members
    def __init__(self, name, balance=0.0,):
        BankAccount.__init__(self, name, balance)
        self.__routingNumber = random.randint(1, 20) ## Random Numbers Generated for Routing Number
        self.__accountNumber = random.randint(1, 10) ## Random Numbers Generated for Account Number

    ## Access to Private Members: 'routingNumbers' and 'accountNumber'
    def getRoutingNumber(self):
        return self.__routingNumber
    def getAccountNumber(self):
        return self.__accountNumber

    ## Assignment Requirements: Adding Intrest
    def interest(self):
        balance = self.getCustomerBalance()
        if balance == 0:
            rate = 0.0
        elif balance < 500:
            rate = 0.02
        else:
            rate = 0.05

        interest = balance * rate
        print(f"Current Balance with {self.getCustomerName()}: {interest:.2f}")