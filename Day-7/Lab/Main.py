'''
Class: Employee
Method: calculateSalary()

Child Classes:
FullTimeEmployee
PartTimeEmployee

Each must calculate salary differently.

Create parent reference (if possible in language)
Call method and observe runtime behavior.
 '''


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculateSalary(self):
        return 0
    
class FullTimeEmployee(Employee):
    def __init__(self, monthlySalary, bonus):
        super().__init__(monthlySalary)
        self.bonus = bonus

    def calculateSalary(self):
        return self.salary+self.bonus
    
class PartTimeEmployee(Employee):
    def __init__(self, hoursWorked, hourlyRate):
        super().__init__(0)
        self.hoursWorked = hoursWorked
        self.hourlyRate = hourlyRate
    
    def calculateSalary(self):
        return self.hoursWorked*self.hourlyRate
    
e1 = FullTimeEmployee(5000, 500)
e2 = PartTimeEmployee(80,20)

print(f"Salary of employee e1: {e1.calculateSalary()}")
print(f"Salary of employee e2: {e2.calculateSalary()}")