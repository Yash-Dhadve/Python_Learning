def find_item(lst, item):
    for i, v in enumerate(lst):
        if v == item:
            return i
    return None

# Usage
result = find_item([1, 2, 3], 2)
print(f"Found at: {result if result is not None else 'Not found'}")

# Default values
value = None or "default"
print(f"Value: {value}")  # "default"