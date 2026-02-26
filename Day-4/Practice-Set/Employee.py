# Create class Employee with method calculateBonus().

class Employee:

    def __init__(self, eName, eSalary, bonusPer):
        self.eName = eName
        self.eSalary = eSalary
        self.bonusPer = bonusPer

    def calculateBonus(self):
        return int(self.eSalary * self.bonusPer / 100)
    

e1 = Employee("Yash", 10000, 5)

print(f"Employee Name: {e1.eName}\nEmployee Salary: {e1.eSalary}\nBonus Percentage: {e1.bonusPer}%\nBonus Amount: {e1.calculateBonus():.2f}")