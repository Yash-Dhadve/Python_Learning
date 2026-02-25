# Print both instance and class variable.

class Var:

    classVar = 0

    def __init__(self):
        self.instanceVar = 0

        

var1 = Var()

print(f"{var1.instanceVar} {var1.classVar}")

var1.instanceVar += 1
Var.classVar += 1

print(f"{var1.instanceVar} {var1.classVar}")