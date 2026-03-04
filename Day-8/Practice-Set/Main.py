'''
Create abstract class Vehicle
Abstract method start()
Create class Car implementing start()
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def start(self):
        print("Car starting....")

c1 = Car()
c1.start()