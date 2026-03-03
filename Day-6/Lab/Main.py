'''
Class: BankAccount

Properties:
accountHolder
balance

Child Class: SavingsAccount
Add interestRate

Method: calculateInterest()
Override method displayDetails()

Test by creating object and calling all methods.
'''

class BankAccount:
    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance
        
    def displayDetails(self):
        print(f"Account Holder: {self.accountHolder}")
        print(f"Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, accountHolder, balance, interestRate):
        super().__init__(accountHolder, balance)
        self.interestRate = interestRate

    def calculateInterest(self):
        return self.balance * self.interestRate / 100 
    
    def displayDetails(self):
        super().displayDetails()
        print(f"Interest Rate: {self.interestRate}")
        print(f"Calculated Interest: {self.calculateInterest()}")


acc1 = SavingsAccount("Yash", 1000, 2)
acc1.displayDetails()