# Create a Laptop class with brand and RAM.

class laptop:
    def __init__(self):
        brand = ""
        RAM = 0

lap1 = laptop()
lap1.brand = "HP"
lap1.RAM = 16

lap2 = laptop()
lap2.brand = "ROG"
lap2.RAM = 32

print(f"Brand: {lap1.brand}")
print(f"RAM: {lap1.RAM} \n")

print(f"Brand: {lap2.brand}")
print(f"RAM: {lap2.RAM}")