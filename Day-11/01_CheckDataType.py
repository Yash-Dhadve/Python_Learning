# Numeric type
count = 42              #int
ration = 3.14           #float
formula = 3 + 4j        #complex

# Boolean type
is_valid = True         # Bool

# Sequence types
name = "Alice"             # str
numbers = [1, 2, 3]         # list
coordinates = (10, 20)      # tuple

# Set types
unique_items = {1,2,3}  # set

# Mapping type
person = {"name": "Alice", "age": 30} # dict

# Bytes types
data = b"Hello"             #bytes
mutable_data = bytearray(b"hello") #bytearray

# Null type
nothing = None # NoneType

#type checking
print(type(count))     # <class 'int'>
print(isinstance(count, int))  # True
