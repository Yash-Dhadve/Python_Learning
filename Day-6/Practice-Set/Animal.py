class Animal:
    def __init__(self,name):
        self.name = name

    def makeSound(self):
        print("Animal makes sound...")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def makeSound(self):
        print("Bow bow...")

dog = Dog("Dog")
print(f"Animal: {dog.name}")
dog.makeSound()