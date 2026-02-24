'''
Create a Product class

Constructor should take:
productName
price
quantity

Then create 2 objects and print total cost:
total = price * quantity
'''

class Product:
    def __init__(self, productName, price, quantity):
        self.productName = productName
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity
    

p1 = Product("ABC", 20, 5)
print(f"Product Name: {p1.productName}")
print(f"Price: {p1.price}")
print(f"Quantity: {p1.quantity}")
print(f"Total: {p1.get_total()}\n")

p2 = Product("XYZ", 10, 4)
print(f"Product Name: {p2.productName}")
print(f"Price: {p2.price}") 
print(f"Quantity: {p2.quantity}")
print(f"Total: {p2.get_total()}")