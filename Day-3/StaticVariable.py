class Student:
    count = 0 # class variable

    def __init__(self):
        Student.count += 1 

s1 = Student()
s2 = Student()
s3 = Student()

print(Student.count)