# Create a Movie class and store name + rating.

class movie:
    def __init__(self):
        name = ""
        rating = 0

mov1 = movie()
mov1.name = "Iron man"
mov1.rating = 5

print(f"Movie Name: {mov1.name}")
print(f"Ratings: {mov1.rating}")