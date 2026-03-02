class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle is starting...")
    

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def start(self):
        print("Car is starting...")

car1 = Car("Toyota")
print(f"Brand: {car1.brand}")
car1.start()