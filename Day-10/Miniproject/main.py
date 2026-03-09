class BankAccount:

    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.__balance = balance

    def deposit(self, amount):
        if(amount > 0): self.__balance += amount
        else: print("Invalid Amount")

    def withdraw(self, amount):
        if(amount <= self.__balance and amount > 0): self.__balance -= amount
        else: print("Invalid Amount")

    def getBalance(self):
        return self.__balance

    def display_details(self):
        print("Account Holder: ",self.accountHolder);
        print("Account Balance: ",self.__balance);


class SavingsAccount(BankAccount):

    def __init__(self, accountHolder, balance, rate):
        super().__init__(accountHolder, balance)
        self.__interestRate = rate

    def calculateInterest(self):
        return self.getBalance() * (self.__interestRate/100)
    
    def display_details(self):
        super().display_details()
        print("Account Interest Rate: ",self.__interestRate);
        print("Calculated Interest: ",self.calculateInterest(),"\n");
    
acc1 = SavingsAccount("Yash Dhadve", 1000, 2)

print("Account Balance: ",acc1.getBalance());
acc1.deposit(500);
print("Account Balance After Depositing: ",acc1.getBalance());
acc1.withdraw(200);
print("Account Balance After Withdraw: ",acc1.getBalance(),"\n");

acc1.display_details()
