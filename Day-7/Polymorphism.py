class Animal:
    def makeSound(self):
        print("Animal sound")

class Dog(Animal):
    def makeSound(self):
        print("Dog barks")

tommy = Dog()
tommy.makeSound()