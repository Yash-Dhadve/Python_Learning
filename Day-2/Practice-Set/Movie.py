# Create a Movie class with name and rating.

class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

m1 = Movie("ABC", 5)
print(f"Movie Name: {m1.name}")
print(f"Rating: {m1.rating}\n")

m2 = Movie("XYZ", 4)
print(f"Movie Name: {m2.name}")
print(f"Rating: {m2.rating}")