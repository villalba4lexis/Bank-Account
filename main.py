class BankAccount:
    customerBank = "Wells Fargo"

    def __init__(self, name, balance=0.0):
        self.customerName = name
        self.customerBalance = balance
        self.customerMinBalance = 50.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit Failed: PLEASE DEPOSIT VALID VALUE.")
        else:
            self.customerBalance += amount
            print(f"Deposit Successful:\n    NEW BALANCE {self.customerBalance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw Failed: PLEASE ENTER VALID VALUE.")
        elif self.customerBalance - amount < self.customerMinBalance:
            print(f"Withdraw Failed:\n    CANNOT WITHDRAW MINIMUM BALANCE: {self.customerMinBalance}.")
        else:
            self.customerBalance -= amount
            print(f"Withdraw Successful: New Balance is {self.customerBalance}")

    def print_customer_information(self):
        print("Bank Account Information")
        print("------------------------------------------")
        print(f"Bank Title: {BankAccount.customerBank}")
        print(f"Customer Name: {self.customerName}")
        print(f"Account Balance: {self.customerBalance}")
        print(f"Minimum Required Balance: {self.customerMinBalance}")

    def __str__(self):
        return (f"Bank Account Information\n"
            f"------------------------------------------\n"
            f"Bank Title: {BankAccount.customerBank}\n"
            f"Customer Name: {self.customerName}\n"
            f"Account Balance: {self.customerBalance}\n"
            f"Minimum Required Balance: {self.customerMinBalance}")

instance1 = BankAccount("Alexis", 500)
instance2 = BankAccount("Claudia", 250)

print(instance1)
print(instance2)