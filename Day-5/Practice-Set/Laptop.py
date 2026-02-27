# Create class Laptop with private price.

class Laptop:

    def __init__(self, brand):
        self.brand = brand
        self.__price = 0

    def setPrice(self, price):
        if price >= 0:
            self.__price = price
            print("Price set successfully.")
        else:
            print("Invalid Price!")

    def getPrice(self):
        return self.__price
    

lap1 = Laptop("HP")
lap1.setPrice(50000)
print(f"Brand: {lap1.brand}, Price: {lap1.getPrice()}")