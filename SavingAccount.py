from BankAccount import BankAccount
import random

class SavingAccount(BankAccount):
    ## Initializing Attributes for SavingAccount Sub-Class w/ Private members
    def __init__(self, name, balance=0.0,):
        BankAccount.__init__(self, name, balance)
        self.__routingNumber = random.randint(1000000000, 9999999999) ## Unique Routing Number
        self.__accountNumber = random.randint(10000000, 99999999) ## Unique Account Number
        self.__balanceAfterInterest = 0.0

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

        interest_amount = balance * rate
        self.__balanceAfterInterest = balance + interest_amount
        print(f"Interest Balance for {self.getCustomerName()}:\n    ${self.__balanceAfterInterest:.2f}")

    def __str__(self):
        return (f"{self.getCustomerBank()} Saving Account Information\n"
                f"------------------------------------------\n"
                f"Customer Name: {self._customerName}\n"
                f"Account Number: {self.__accountNumber}\n"
                f"Routing Number: {self.__routingNumber}\n"
                f"Current Balance: ${self._customerBalance:.2f}\n"
                f"Balance After Interest: ${self.__balanceAfterInterest:.2f}\n")
