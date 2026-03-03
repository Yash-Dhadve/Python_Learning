'''
Create class Vehicle with method start()
Create class Bike overriding start()
'''

class Vehicle:
    def start(self):
        print("Starting Vehicle...")
    
class Bike(Vehicle):
    def start(self):
        print("Starting Bike...")
    

v1 = Vehicle()
b1 = Bike()

v1.start()
b1.start()

