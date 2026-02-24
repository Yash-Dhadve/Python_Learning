# Create a Movie class with name and rating.

class movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

lap1 = movie("ABC", 5)
print(f"Movie Name: {lap1.name}")
print(f"Rating: {lap1.rating}\n")

lap2 = movie("XYZ", 4)
print(f"Movie Name: {lap2.name}")
print(f"Rating: {lap2.rating}")