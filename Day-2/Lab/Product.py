'''
Create a Product class

Constructor should take:
productName
price
quantity

Then create 2 objects and print total cost:
total = price * quantity
'''

class product:
    def __init__(self, productName, price, quantity):
        self.productName = productName
        self.price = price
        self.quantity = quantity
        self.total = price*quantity

p1 = product("ABC", 20, 5)
print(f"Laptop Brand: {p1.productName}")
print(f"Price: {p1.price}")
print(f"Quantity: {p1.quantity}")
print(f"Total: {p1.total}\n")

p2 = product("XYZ", 10, 4)
print(f"Laptop Brand: {p2.productName}")
print(f"Price: {p2.price}")
print(f"Quantity: {p2.quantity}")
print(f"Total: {p2.total}")