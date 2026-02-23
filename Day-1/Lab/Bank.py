'''/*Create a Bank class

Properties:
accountHolder
balance

Create object and print details.
(No methods yet — only properties)'''

class Bank:
    def __init__(self):
        accountHolder = ""
        balance = 0

acc1 = Bank()
acc1.accountHolder = "Yash"
acc1.balance = 1000

acc2 = Bank()
acc2.accountHolder = "Lara"
acc2.balance = 1500

print(f"Account Holder Name: {acc1.accountHolder}")
print(f"Account Balance: {acc1.balance}\n")

print(f"Account Holder Name: {acc2.accountHolder}")
print(f"Account Balance: {acc2.balance}")