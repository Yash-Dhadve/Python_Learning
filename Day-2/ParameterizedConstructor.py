class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s0 = Student("Yash", 80)
print(f"Default Name: {s0.name}")
print(f"Default Marks: {s0.marks}")