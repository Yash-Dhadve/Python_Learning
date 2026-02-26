'''
Class: BankAccount

Properties:
accountHolder
balance

Methods:
deposit(amount)
withdraw(amount)
checkBalance()

Create 1 object and test all methods.
'''

class BankAccount:

    def __init__(self, accountHolder):
        self.accountHolder = accountHolder
        self.balance = 1000

    def deposit(self, amount):
        if(amount > 0):
            self.balance += amount
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if(amount > 0 and amount <= self.balance):
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Invalid or insufficient balance!")

    def checkBalance(self):
        print(f"Account Balance: {self.balance}")
    
acc1 = BankAccount("Yash")

print(f"Account Holder: {acc1.accountHolder}\nBalance: {acc1.balance}\n")

print("\nDepositing 500...")
acc1.deposit(500)
print(f"Account Holder: {acc1.accountHolder}\nBalance: {acc1.balance}\n")

print("\nWithdrawing 200...")
acc1.withdraw(200)
print(f"Account Holder: {acc1.accountHolder}\nBalance: {acc1.balance}\n")

print("\nChecking Balance...")
acc1.checkBalance()
print(f"Account Holder: {acc1.accountHolder}\nBalance: {acc1.balance}\n")