# Create a Laptop class with brand and price using __init__.

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

lap1 = Laptop("HP", 60000)
print(f"Laptop Brand: {lap1.brand}")
print(f"Price: {lap1.price}\n")

lap2 = Laptop("ROG", 100000)
print(f"Laptop Brand: {lap2.brand}")
print(f"Price: {lap2.price}")