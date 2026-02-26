# Create class ATM with method withdraw().

class ATM:

    def __init__(self, accountHolder):
        self.accountHolder = accountHolder
        self.balance = 1000

    def withdraw(self,amount):
        if (self.balance>=amount):
            self.balance -= amount
            print("Amount Withdrawal Successful\n")
        else:
            print("Insufficient Balance!\n") 

acc1 = ATM("Yash")

print(f"Account Holder Name: {acc1.accountHolder}\nBalance: {acc1.balance}\n")

acc1.withdraw(100)
print(f"Account Holder Name: {acc1.accountHolder}\nBalance: {acc1.balance}")
