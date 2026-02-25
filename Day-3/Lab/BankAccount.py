'''
Class: BankAccount

Instance variables:
accountHolder
balance

Static/Class variable:
bankName = "SBI"

Create 3 accounts and print:
Account holder
Bank name
Total accounts created
'''

class BankAccount:
    bankName = "SBI"
    count = 0

    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance
        BankAccount.count += 1


acc1 = BankAccount("Yash", 1000)
acc2 = BankAccount("Lara", 1500)
acc3 = BankAccount("Pavii", 2000)

print(f"Account Holder: {acc1.accountHolder}")
print(f"Balance: {acc1.balance}")
print(f"Bank Name: {BankAccount.bankName} \n")

print(f"Account Holder: {acc2.accountHolder}")
print(f"Balance: {acc2.balance}")
print(f"Bank Name: {BankAccount.bankName} \n")

print(f"Account Holder: {acc3.accountHolder}")
print(f"Balance: {acc3.balance}")
print(f"Bank Name: {BankAccount.bankName} \n")

print(f"Total Bank Accounts: {BankAccount.count}")