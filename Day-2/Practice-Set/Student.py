# Create a Student class and pass name, age, marks.

class student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

s1 = student("Yash", 5, 80)
print(f"Student Name: {s1.name}")
print(f"Age: {s1.age}")
print(f"Marks: {s1.marks}\n")

s2 = student("Lara", 4, 75)
print(f"Student Name: {s2.name}")
print(f"Age: {s2.age}")
print(f"Marks: {s2.marks}")
