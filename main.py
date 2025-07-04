from BankAccount import BankAccount
from SavingAccount import SavingAccount
from CheckingAccount import CheckingAccount

## Bank Account Initialization
customerBankAccount = BankAccount("Jonathan") ## Bank Account Instance, Only added name parameter
print(f"{customerBankAccount}\n")
customerBankAccount.deposit(500.00) ## Depositing Success
customerBankAccount.deposit(-10) ## Depositing Error
print("")
customerBankAccount.withdraw(50.55) ## Withdraw Success
customerBankAccount.withdraw(-9999)  ## Withdraw Fail
print("")
print(f"Customer Final Balance: {customerBankAccount.getCustomerBalance()}\n")

## Saving Account Initialization
customerSavingAccount = SavingAccount("Alex") ## First Saving Account Instance, Only added name parameter
print(f"\n{customerSavingAccount}")
customerSavingAccount.deposit(2000.20) ## Depositing, in order to see intrest change
customerSavingAccount.interest()
customerSavingAccount2 = SavingAccount("Maria", 52239.21) ## Second Saving Account Instance, Added both parameters
print(f"\n{customerSavingAccount2}")

## Checking Account Initialization
customerCheckingAccount = CheckingAccount("Maxwell", 10) ## First Checking Account Instance, Added both parameters
print(f"\n{customerCheckingAccount}\n")
customerCheckingAccount.depositLimit(500.00) # Deposit Limit, does not exceed limit
customerCheckingAccount.depositLimit(200.00) # Deposit Limit, does not exceed limit
customerCheckingAccount.depositLimit(40000) # Deposit Limit, exceeds limit
# Every time deposit is added, it adds to the instance variable total balance
# Checking Account Initialization
customerCheckingAccount2 = CheckingAccount("Kamala", 50) ## Second Checking Account Instance, Added both parameters
print(f"\n{customerCheckingAccount2}\n")
customerCheckingAccount2.depositLimit(50000) # Deposit Limit, exceeds limit
