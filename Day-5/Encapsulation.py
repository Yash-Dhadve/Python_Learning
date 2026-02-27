class bank:
    def __init__(self):
        self.__balance = 0

    def setBalance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount!")

    def getBalance(self):
        return self.__balance
    
b = bank()
b.setBalance(500)
print(f"Balance: {b.getBalance()}")