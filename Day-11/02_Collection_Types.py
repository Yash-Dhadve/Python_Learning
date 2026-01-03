# Set operations
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(f"Union: {s1 | s2}")           # {1, 2, 3, 4}
print(f"Intersection: {s1 & s2}")    # {2, 3}
print(f"Difference: {s1 - s2}")      # {1}

# Dict operations
person = {"name": "Alice", "age": 30, "city": "NYC"}
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")
print(f"Get with default: {person.get('job', 'Unknown')}")

# Dict comprehension
squares = {x: x**2 for x in range(5)}
print(f"Squares: {squares}")