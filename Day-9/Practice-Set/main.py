'''
Create class Flyable and Swimmable
Create class duck using both'''

class Flyable:
    def fly(self):
        print("Fly...")

class Swimmable:
    def swim(self):
        print("Swim...")

class duck(Flyable, Swimmable):
    pass

d1 = duck()
d1.fly()
d1.swim()