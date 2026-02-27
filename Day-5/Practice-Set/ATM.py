# Create class ATM with private balance and validate withdrawal.

class ATM:
    def __init__(self):
        self.__balance = 0

    def setBalance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print("Balance set successfully.")
        else:
            print("Invalid amount!")

    def getBalance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

acc1 = ATM()
acc1.setBalance(5000)
print(f"Current Balance: {acc1.getBalance()}")
acc1.withdraw(2000)
print(f"Balance after withdrawal: {acc1.getBalance()}")
acc1.withdraw(4000)  
