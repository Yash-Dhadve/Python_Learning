class Car:
    def __init__(self):
        self.brand = ""
        self.speed = 0

car1 = Car()
car1.brand = "BMW"
car1.speed = 130

print(f"Brand: {car1.brand}")
print(f"Speed: {car1.speed} km/h")