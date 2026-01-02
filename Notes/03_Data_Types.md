# Data Types

## 1. Introduction

*Definition*

Data types represent the kind of value a variable holds and define what operations can be performed on that value. Python supports multiple built-in data types organized into categories: numeric (`int`, `float`, `complex`), boolean (`bool`), sequence (`str`, `list`, `tuple`), set (`set`), mapping (`dict`), bytes sequence (`bytes`, `bytearray`), and null (`NoneType`).

*Why used*

- Determines memory allocation and operations available.
- Enables type checking and data validation.
- Affects performance and memory efficiency.
- Critical for API design and function contracts.

*Real-world usage*

- Integers: counters, IDs, indices, loop variables.
- Floats: measurements, currency, scientific calculations.
- Strings: text data, user input, file contents, JSON parsing.
- Lists: collections of items, stacks, queues, dynamic arrays.
- Dictionaries: key-value storage, JSON data, caching, config files.
- Sets: membership testing, deduplication, mathematical operations.
- Tuples: immutable sequences, function returns, dict keys.
- Bytes: binary data, file I/O, network communication.
- Complex: electrical engineering, signal processing, physics simulations.

*Advantages*

- Diverse types support various programming paradigms.
- Dynamic typing allows flexibility and rapid prototyping.
- Rich data structure options for different use cases.
- Immutable types (tuple, frozenset, str) enable safe sharing and caching.

*Disadvantages*

- Dynamic typing can hide type errors until runtime.
- Mutable types (list, dict, set) require careful handling to avoid side effects.
- Memory overhead for flexibility compared to statically-typed languages.
- Type conversions can be surprising (e.g., `bool("False")` is `True`).

---

## 2. Syntax / Basic Structure

```python
# data_types_overview.py - demonstrating basic data types
# Numeric types
count = 42              # int
ratio = 3.14           # float
formula = 3 + 4j       # complex

# Boolean type
is_valid = True        # bool

# Sequence types
name = "Alice"         # str
numbers = [1, 2, 3]    # list
coordinates = (10, 20) # tuple

# Set type
unique_items = {1, 2, 3}  # set

# Mapping type
person = {"name": "Alice", "age": 30}  # dict

# Bytes types
data = b"hello"        # bytes
mutable_data = bytearray(b"hello")  # bytearray

# Null type
nothing = None         # NoneType

# Type checking
print(type(count))     # <class 'int'>
print(isinstance(count, int))  # True
```

Explanation line-by-line:
- `count = 42` — integer literal.
- `ratio = 3.14` — floating-point literal.
- `formula = 3 + 4j` — complex number (3 + 4i in math notation).
- `is_valid = True` — boolean literal.
- `name = "Alice"` — string literal.
- `numbers = [1, 2, 3]` — list literal.
- `coordinates = (10, 20)` — tuple literal.
- `unique_items = {1, 2, 3}` — set literal.
- `person = {"name": "Alice", "age": 30}` — dict literal.
- `data = b"hello"` — bytes literal (prefix `b`).
- `mutable_data = bytearray(b"hello")` — mutable bytes.
- `nothing = None` — null reference.
- `type(x)` — returns type of object.
- `isinstance(x, type)` — checks if object is instance of type.

---

## 3. Core Concepts

### int (Integer)
- Definition: Whole numbers without decimal point, positive, negative, or zero.
- Explanation: Arbitrary precision (unlimited size); supports binary (`0b`), octal (`0o`), hexadecimal (`0x`) literals.
- Syntax:
  - Decimal: `42`, `-5`
  - Binary: `0b1010` (10 in decimal)
  - Octal: `0o755` (493 in decimal)
  - Hexadecimal: `0xFF` (255 in decimal)
- Parameters / Return values: N/A.
- Internal working: Stored as variable-length integer object; supports arbitrary precision via memory allocation.
- Use cases: Counters, indices, IDs, mathematical operations.
- Important notes:
  - No overflow (unlike C/Java); grows dynamically.
  - Division with `/` returns float; use `//` for integer division.
  - `divmod(a, b)` returns quotient and remainder as tuple.

### float (Floating-Point)
- Definition: Numbers with decimal point; approximation of real numbers.
- Explanation: Follows IEEE 754 standard; limited precision (usually 15-17 significant digits).
- Syntax:
  - Decimal: `3.14`, `-0.5`
  - Scientific: `1.5e2` (150.0), `2e-3` (0.002)
- Parameters / Return values: N/A.
- Internal working: Stored as binary fraction; limited precision causes rounding errors.
- Use cases: Measurements, calculations, financial data (with caution).
- Important notes:
  - Avoid equality comparisons (`==`); use `abs(a - b) < epsilon` for tolerance.
  - `float('inf')`, `float('-inf')`, `float('nan')` are valid.
  - Operations may accumulate precision errors.

### complex (Complex Number)
- Definition: Number with real and imaginary parts; represented as `a + bj`.
- Explanation: `j` suffix denotes imaginary unit (sqrt(-1)); supports arithmetic operations.
- Syntax:
  - `3 + 4j` — 3 is real, 4 is imaginary.
  - `complex(3, 4)` — constructor form.
- Parameters / Return values: N/A.
- Internal working: Two floats (real and imaginary) packaged together.
- Use cases: Electrical engineering, signal processing, physics.
- Important notes:
  - Attributes: `.real`, `.imag`, `.conjugate()`.
  - No ordering (`<`, `>`) on complex numbers.

### bool (Boolean)
- Definition: Logical value `True` or `False`.
- Explanation: Subclass of `int` (`True == 1`, `False == 0`); used for conditionals and truth testing.
- Syntax:
  - `True`, `False` (keywords)
  - `bool(value)` — constructor; follows truthiness rules.
- Parameters / Return values: N/A.
- Internal working: `True` is `1`, `False` is `0` internally.
- Use cases: Conditionals, boolean logic, flags.
- Important notes:
  - Truthiness: empty containers, 0, None, False are falsy; everything else truthy.
  - Boolean operators: `and`, `or`, `not` (short-circuit evaluation).

### str (String)
- Definition: Immutable sequence of Unicode characters.
- Explanation: Enclosed in single, double, or triple quotes; supports escape sequences and f-strings.
- Syntax:
  - Single: `'hello'`
  - Double: `"world"`
  - Triple: `'''multi\nline'''`
  - Raw: `r'C:\path'` (backslashes literal)
- Parameters / Return values: N/A.
- Internal working: Stored as immutable Unicode characters; optimized internally (interning).
- Use cases: Text data, file I/O, configuration, output formatting.
- Important notes:
  - Indexing: `s[0]` first char, `s[-1]` last char.
  - Slicing: `s[start:end:step]` extracts substring.
  - Methods: `.upper()`, `.lower()`, `.split()`, `.join()`, `.replace()`, `.strip()`, etc.

### list (List)
- Definition: Mutable, ordered sequence of elements (any types mixed).
- Explanation: Supports insertion, deletion, modification; most used collection type.
- Syntax:
  - `[1, 2, 3]` — list literal.
  - `[x for x in range(5)]` — list comprehension.
  - `list('abc')` — constructor.
- Parameters / Return values: N/A.
- Internal working: Dynamic array; resizes as needed; supports random access O(1).
- Use cases: Storing collections, stacks, queues, dynamic arrays.
- Important notes:
  - Mutable: `list[0] = new_value` modifies.
  - Methods: `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`, etc.
  - List comprehensions are Pythonic and efficient.
Answer: Provide a concise explanation or implement the requested logic based on the question.

### tuple (Tuple)
- Definition: Immutable, ordered sequence of elements.
- Explanation: Fixed size; cannot add, remove, or modify elements after creation.
- Syntax:
  - `(1, 2, 3)` — tuple literal.
  - `1, 2, 3` — implicit tuple (parentheses optional).
  - `(1,)` — single-element tuple (comma required).
  - `tuple([1, 2, 3])` — constructor.
- Parameters / Return values: N/A.
- Internal working: Fixed-size immutable sequence; hashable (can be dict key or set member).
- Use cases: Function returns, dict keys, immutable collections.
- Important notes:
  - Indexing and slicing like lists.
  - Cannot modify; creates new tuple for changes.
  - Unpacking: `a, b = (1, 2)`.
  - Methods: `.count()`, `.index()` only.

### set (Set)
- Definition: Unordered collection of unique, hashable elements.
- Explanation: No duplicates; fast membership testing; supports mathematical set operations.
- Syntax:
  - `{1, 2, 3}` — set literal.
  - `set([1, 2, 3])` — constructor (converts list to set).
  - `set()` — empty set (not `{}`; that's empty dict).
- Parameters / Return values: N/A.
- Internal working: Hash table-based; O(1) average membership testing.
- Use cases: Deduplication, membership testing, set operations (union, intersection).
- Important notes:
  - Mutable: `.add()`, `.remove()`, `.discard()`.
  - Operations: `|` (union), `&` (intersection), `-` (difference), `^` (symmetric difference).
  - `frozenset()` is immutable variant.

### dict (Dictionary)
- Definition: Mutable, unordered (in Python 3.7+ insertion-ordered) mapping of keys to values.
- Explanation: Key-value pairs; keys must be hashable; fast lookup O(1) average.
- Syntax:
  - `{"name": "Alice", "age": 30}` — dict literal.
  - `dict(name="Alice", age=30)` — constructor.
  - `{k: v for k, v in pairs}` — dict comprehension.
- Parameters / Return values: N/A.
- Internal working: Hash table; keys hashed to find values.
- Use cases: Configuration, JSON data, caching, counters.
- Important notes:
  - Mutable: `dict[key] = value` assigns.
  - Methods: `.keys()`, `.values()`, `.items()`, `.get()`, `.pop()`, `.update()`, etc.
  - KeyError if accessing non-existent key; use `.get(key, default)` safely.

### bytes (Bytes)
- Definition: Immutable sequence of bytes (0-255 integers).
- Explanation: Represents binary data; often from files, network, encoding.
- Syntax:
  - `b'hello'` — bytes literal.
  - `bytes([72, 101, 108, 108, 111])` — constructor.
  - `'hello'.encode('utf-8')` — encoding string to bytes.
- Parameters / Return values: N/A.
- Internal working: Fixed sequence of bytes; immutable and hashable.
- Use cases: File I/O, network data, encoded strings.
- Important notes:
  - Indexing returns int: `b'hello'[0]` is `104` (ASCII for 'h').
  - Decoding: `bytes_obj.decode('utf-8')` converts to string.
  - Methods: `.decode()`, `.hex()`, `.startswith()`, etc.

### bytearray (Bytearray)
- Definition: Mutable sequence of bytes.
- Explanation: Like bytes but mutable; supports item assignment.
- Syntax:
  - `bytearray(b'hello')` — constructor.
  - `bytearray(5)` — creates zero-filled array of size 5.
- Parameters / Return values: N/A.
- Internal working: Mutable byte array; resizable.
- Use cases: Modifying binary data in-place, building binary messages.
- Important notes:
  - Mutable: `ba[0] = 65` modifies.
  - Methods: `.append()`, `.extend()`, `.remove()`, `.reverse()`, `.decode()`, etc.
  - Not hashable (cannot be dict key).

### NoneType (None)
- Definition: Null/absence value; represents no value.
- Explanation: Singleton; only one `None` exists in Python.
- Syntax:
  - `None` (keyword)
  - `type(None)` returns `<class 'NoneType'>`
- Parameters / Return values: N/A.
- Internal working: Single global object.
- Use cases: Default return value, flag for missing data, initializing variables.
- Important notes:
  - Falsy: `if None:` is False.
  - Check with `is None`, not `== None` (more efficient, idiomatic).
  - Functions without explicit return implicitly return `None`.

---

## 4. Subtopics

### Numeric Types: int, float, complex
- Explanation: Numbers used for arithmetic and calculations.
- Syntax examples:
```python
a = 10              # int
b = 3.14            # float
c = 2 + 3j          # complex
d = int("42")       # conversion
e = float("3.14")   # conversion
```
- Example:
```python
x, y = 5, 2
print(f"Sum: {x + y}")          # 7
print(f"Int division: {x // y}") # 2
print(f"Float division: {x / y}") # 2.5
print(f"Power: {x ** y}")        # 25
z = 3 + 4j
print(f"Magnitude: {abs(z)}")    # 5.0
```
Output:
```
Sum: 7
Int division: 2
Float division: 2.5
Power: 25
Magnitude: 5.0
```
- Edge cases:
  - Division by zero raises `ZeroDivisionError`.
  - Float precision errors in comparison.
  - Complex numbers don't support ordering.
- Interview questions:
  - Explain integer division vs float division.
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - Why does `0.1 + 0.2 != 0.3` in floating-point?
Answer: Provide a concise explanation or implement the requested logic based on the question.

### Boolean Type and Truthiness
- Explanation: Logical values and truth testing.
- Syntax:
```python
is_valid = True
is_empty = False
result = bool(10)  # True (non-zero is truthy)
result = bool(0)   # False
result = bool([])  # False (empty collection is falsy)
```
- Example:
```python
values = [0, 1, "", "hello", [], [1, 2], None, False, True]
for v in values:
    print(f"{repr(v):15} => {bool(v)}")
```
Output:
```
0               => False
1               => True
''              => False
'hello'         => True
[]              => False
[1, 2]          => True
None            => False
False           => False
True            => True
```
- Edge cases:
  - Empty collections, 0, None, False are falsy.
  - Non-empty collections, non-zero numbers, True, non-empty strings are truthy.
- Interview questions:
  - What makes a value truthy or falsy?
Answer: Truthy values evaluate to True in Boolean contexts, while falsy values evaluate to False; examples include non-empty strings and zero, respectively.
  - Why is `bool("False")` True?
Answer: Provide a concise explanation or implement the requested logic based on the question.

### String Type: Immutability and Methods
- Explanation: Immutable text data with rich method support.
- Syntax:
```python
s = "hello"
s_upper = s.upper()     # new string
s_replaced = s.replace("l", "L")  # new string
s_split = s.split("l")  # list
```
- Example:
```python
text = "  Python Programming  "
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Upper: '{text.upper()}'")
print(f"Split: {text.split()}")
print(f"Replaced: {text.replace('Python', 'Java')}")
print(f"Find index: {text.find('Pro')}")
```
Output:
```
Original: '  Python Programming  '
Stripped: 'Python Programming'
Upper: '  PYTHON PROGRAMMING  '
Split: ['Python', 'Programming']
Replaced: '  Java Programming  '
Find index: 2
```
- Edge cases:
  - Immutable: operations return new strings; original unchanged.
  - Indexing: `s[0]` first char, `s[-1]` last char; negative indices count from end.
- Interview questions:
  - Why are strings immutable in Python?
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - How do you reverse a string?
Answer: Provide a concise explanation or implement the requested logic based on the question.

### Sequence Types: list, tuple, and Slicing
- Explanation: Ordered collections accessed by index.
- Syntax:
```python
lst = [1, 2, 3, 4, 5]
lst[0]      # 1 (first element)
lst[-1]     # 5 (last element)
lst[1:4]    # [2, 3, 4] (slice)

---

## Additional: Identity, Mutability and Type Utilities

### Mutable vs Immutable
- Definition: Explain what it means for an object to be mutable or immutable.
- Explanation: How mutability affects copying, function arguments, and performance.
- Syntax / Examples:
```python
# Immutable
s = "hello"
s2 = s.replace('h','H')
# Mutable
l = [1,2,3]
l.append(4)
```
- Internal Working: Object internals, optimizations, and memory implications.
- Example: show mutation vs reassignment and effect on references.
- Output: Provide expected outputs for examples.
- Real World Use Case: When to prefer tuples vs lists.
- Advantages / Disadvantages / Common Mistakes / Best Practices / Interview Q&A / Exercises / Output Questions / Revision Notes

### `id()`, `type()`, `isinstance()`
- Definition: Purpose of each function.
- Explanation: Differences between `type()` and `isinstance()`, and when to use `id()`.
- Syntax / Examples:
```python
obj = [1,2]
print(id(obj))
print(type(obj))
print(isinstance(obj, list))
```
- Internal Working: Identity vs value semantics.
- Example / Output / Use Cases / Advantages / Disadvantages / Common Mistakes / Best Practices / Interview Q&A / Exercises / Output Questions / Revision Notes

### Identity vs Equality
- Definition: `is` vs `==` semantics.
- Explanation: When `is` is appropriate (singleton checks) and pitfalls of using `is` for value equality.
- Syntax / Examples:
```python
a = [1,2]
b = a
c = [1,2]
print(a is b)   # True
print(a == c)   # True
print(a is c)   # False
```
- Internal Working: Object identity, interning, and caching.
- Example / Output / Use Cases / Advantages / Disadvantages / Common Mistakes / Best Practices / Interview Q&A / Exercises / Output Questions / Revision Notes
lst[::2]    # [1, 3, 5] (every 2nd element)
lst[::-1]   # [5, 4, 3, 2, 1] (reversed)
```
- Example:
```python
data = [10, 20, 30, 40, 50]
print(f"First: {data[0]}")
print(f"Last: {data[-1]}")
print(f"Middle: {data[1:4]}")
print(f"Reversed: {data[::-1]}")

# Tuple unpacking
a, b, c = (1, 2, 3)
print(f"Unpacked: a={a}, b={b}, c={c}")

# Tuple as function return
def get_coords():
    return (10, 20)
x, y = get_coords()
print(f"Coordinates: {x}, {y}")
```
Output:
```
First: 10
Last: 50
Middle: [30, 40]
Reversed: [50, 40, 30, 20, 10]
Unpacked: a=1, b=2, c=3
Coordinates: 10, 20
```
- Edge cases:
  - Lists mutable; tuples immutable.
  - Slicing with negative indices: `s[-3:-1]` or `s[:-1]`.
  - Out-of-range slicing doesn't error; returns partial slice.
- Interview questions:
  - Explain the difference between list and tuple.
Answer: Explain how the two concepts differ in behavior, use cases, and effect on program state.
  - How do you slice a list from the end?
Answer: Provide a concise explanation or implement the requested logic based on the question.

### Collection Types: set and dict
- Explanation: Unordered collections and key-value mappings.
- Syntax:
```python
s = {1, 2, 3}
d = {"a": 1, "b": 2}
s.add(4)              # modifies set
d["c"] = 3            # modifies dict
1 in s                # True (membership)
"a" in d              # True (key check)
```
- Example:
```python
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
```
Output:
```
Union: {1, 2, 3, 4}
Intersection: {2, 3}
Difference: {1}
Keys: ['name', 'age', 'city']
Values: ['Alice', 30, 'NYC']
Items: [('name', 'Alice'), ('age', 30), ('city', 'NYC')]
Get with default: Unknown
Squares: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```
- Edge cases:
  - Sets require hashable elements; lists not allowed.
  - Dict keys must be hashable; values can be any type.
  - Iterating dicts iterates keys, not values.
- Interview questions:
  - When would you use a set vs a list?
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - How do you safely access a dict key that might not exist?
Answer: Provide a concise explanation or implement the requested logic based on the question.

### Bytes and bytearray Types
- Explanation: Binary data handling.
- Syntax:
```python
b = b"hello"
ba = bytearray(b"hello")
text = "hello"
encoded = text.encode("utf-8")  # bytes
decoded = encoded.decode("utf-8")  # str
```
- Example:
```python
# Encoding and decoding
text = "Hello, 世界"
encoded = text.encode("utf-8")
print(f"Encoded: {encoded}")
print(f"Decoded: {encoded.decode('utf-8')}")

# Bytearray manipulation
ba = bytearray(b"hello")
ba[0] = ord('H')  # change first byte
print(f"Modified: {ba}")
ba.append(ord('!'))
print(f"Appended: {ba}")

# Hex representation
print(f"Hex: {encoded.hex()}")
```
Output:
```
Encoded: b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
Decoded: Hello, 世界
Modified: bytearray(b'Hello')
Appended: bytearray(b'Hello!')
Hex: 48656c6c6f2c20e4b896e7958c
```
- Edge cases:
  - Indexing bytes returns int (0-255), not char.
  - Bytearray is mutable; bytes is immutable and hashable.
  - Unicode encoding issues if wrong charset assumed.
- Interview questions:
  - What is the difference between bytes and bytearray?
Answer: Explain how the two concepts differ in behavior, use cases, and effect on program state.
  - How do you convert a string to bytes and back?
Answer: Provide a concise explanation or implement the requested logic based on the question.

### Type Checking and Conversion
- Explanation: Determining and converting between types.
- Syntax:
```python
type(x)             # returns type object
isinstance(x, int)  # boolean check
int(x)              # conversion
float(x)            # conversion
str(x)              # conversion
list(x)             # conversion
```
- Example:
```python
values = [42, 3.14, "hello", [1, 2], {"a": 1}]
for v in values:
    print(f"{repr(v):20} type: {type(v).__name__:10} isinstance(int): {isinstance(v, int)}")

# Type conversion
print(f"int('42'): {int('42')}")
print(f"float('3.14'): {float('3.14')}")
print(f"str(42): {str(42)}")
print(f"list('abc'): {list('abc')}")
print(f"tuple([1, 2, 3]): {tuple([1, 2, 3])}")
```
Output:
```
42                   type: int        isinstance(int): True
3.14                 type: float      isinstance(int): False
'hello'              type: str        isinstance(int): False
[1, 2]               type: list       isinstance(int): False
{'a': 1}             type: dict       isinstance(int): False
int('42'): 42
float('3.14'): 3.14
str(42): 42
list('abc'): ['a', 'b', 'c']
tuple([1, 2, 3]): (1, 2, 3)
```
- Edge cases:
  - Invalid conversions raise ValueError.
  - `bool(x)` follows truthiness rules.
  - `isinstance()` returns True for subclasses; `type()` is exact.
- Interview questions:
  - When would you use `isinstance()` vs `type()`?
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - Why does `int("3.14")` fail?
Answer: Provide a concise explanation or implement the requested logic based on the question.

### None Type
- Explanation: Representing absence or null value.
- Syntax:
```python
x = None
if x is None:  # idiomatic check
    print("x is None")

def foo():
    pass  # implicitly returns None
```
- Example:
```python
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
```
Output:
```
Found at: 1
Value: default
```
- Edge cases:
  - Always use `is None`, not `== None` (though `== None` works).
  - Falsy in boolean context.
  - Functions without return statement implicitly return None.
- Interview questions:
  - Why use `is None` instead of `== None`?
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - What functions return None implicitly?
Answer: Provide a concise explanation or implement the requested logic based on the question.

---

## 5. Examples

### Beginner example — Mixed data types
```python
# person_info.py
name = "Alice"
age = 30
height = 5.9
is_student = False

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Student: {is_student} (type: {type(is_student).__name__})")
```
Output:
```
Name: Alice (type: str)
Age: 30 (type: int)
Height: 5.9 (type: float)
Student: False (type: bool)
```

### Intermediate example — Collections and operations
```python
# collections.py
# Lists and tuples
scores = [85, 90, 78, 92, 88]
best_score = max(scores)
avg_score = sum(scores) / len(scores)
print(f"Scores: {scores}")
print(f"Best: {best_score}, Average: {avg_score:.2f}")

# Sets
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = set(numbers)
print(f"Unique: {unique}")

# Dictionaries
students = {
    "alice": 85,
    "bob": 90,
    "charlie": 78
}
for name, score in students.items():
    print(f"{name}: {score}")
```
Output:
```
Scores: [85, 90, 78, 92, 88]
Best: 92, Average: 86.60
Unique: {1, 2, 3, 4}
alice: 85
bob: 90
charlie: 78
```

### Real-world example — Data processing with mixed types
```python
# data_processing.py
import json

# Complex data structure
users = [
    {"id": 1, "name": "Alice", "tags": {"role": "admin", "active": True}},
    {"id": 2, "name": "Bob", "tags": {"role": "user", "active": True}},
    {"id": 3, "name": "Charlie", "tags": {"role": "user", "active": False}}
]

# Processing
active_admins = [
    u["name"] for u in users
    if u["tags"]["active"] and u["tags"]["role"] == "admin"
]
print(f"Active admins: {active_admins}")

# JSON serialization
data_json = json.dumps(users, indent=2)
print(f"JSON:\n{data_json[:100]}...")
```
Output:
```
Active admins: ['Alice']
JSON:
[
  {
    "id": 1,
    "name": "Alice",
    "tags": {
      "role": "admin",
...
```

### Mini practical example — Type validation
```python
# validate.py
def validate_age(age_input):
    try:
        age = int(age_input)
        if age < 0 or age > 150:
            return None, "Age must be between 0 and 150"
        return age, None
    except ValueError:
        return None, "Invalid input; must be an integer"

# Test
test_inputs = ["25", "invalid", "-5", "200"]
for inp in test_inputs:
    age, error = validate_age(inp)
    if error:
        print(f"'{inp}': Error - {error}")
    else:
        print(f"'{inp}': Valid age {age}")
```
Output:
```
'25': Valid age 25
'invalid': Error - Invalid input; must be an integer
'-5': Error - Age must be between 0 and 150
'200': Error - Age must be between 0 and 150
```

---

## 6. Common Errors and Mistakes

- Typical beginner mistakes:
  - Confusing `=` (assignment) with `==` (comparison).
  - Forgetting that lists are mutable; modifying list affects all references.
  - Using `{}` for empty set instead of `set()`; `{}` is empty dict.
  - Comparing floats with `==` instead of tolerance check.
  - Assuming dict maintains insertion order (true in 3.7+, but not guaranteed in earlier versions).
  - Indexing lists with out-of-range index raises `IndexError`.
  - Modifying dict or set while iterating (causes `RuntimeError`).
  - Assuming None is falsy but comparing with `== None` instead of `is None`.
- Debugging tips:
  - Use `type()` and `isinstance()` to debug type confusion.
  - Print intermediate values to verify data structure contents.
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - Use `repr()` to see exact string representation (e.g., `repr([1, 2])` shows `[1, 2]`).
  - Avoid mutable default arguments in functions.
- Wrong vs correct example — list mutation:

Wrong:
```python
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)  # [1, 2, 3, 4] - original also modified!
```

Correct:
```python
original = [1, 2, 3]
copy = original.copy()  # or list(original)
copy.append(4)
print(original)  # [1, 2, 3] - original unchanged
```

---

## 7. Best Practices

- Industry practices:
  - Use type hints to document expected types: `def greet(name: str) -> str:`.
  - Prefer immutable types (tuple, frozenset) where modifications not needed.
  - Use `collections.defaultdict` or `.get()` for safer dict access.
  - Validate user input and convert to correct type early.
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - Use `None` as default for optional parameters; check with `is None`.
- Clean code tips:
  - Use descriptive variable names that indicate type (e.g., `user_ids` for list, `user_by_id` for dict).
  - Avoid deeply nested data structures; consider custom classes.
  - Use f-strings for readable formatting.
  - Keep functions focused; avoid mixing multiple data types if possible.
- Optimization tips:
  - Use sets for membership testing; O(1) vs O(n) for lists.
  - Use dict for fast lookups by key.
  - List comprehensions are faster than loops for building lists.
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - `tuple` unpacking is efficient for function returns.
- Readability improvements:
  - Use meaningful variable names.
  - Consider dataclasses or namedtuples for structured data.
  - Comment complex type relationships.

---

## 8. Interview Preparation

- Frequently asked interview questions:
  - Explain the difference between list and tuple.
Answer: Explain how the two concepts differ in behavior, use cases, and effect on program state.
  - Why is `None` used instead of null or undefined?
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - How do you check if a dict has a specific key?
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - Explain mutable vs immutable types and give examples.
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - What is the difference between `==` and `is`?
Answer: Explain how the two concepts differ in behavior, use cases, and effect on program state.
  - How do you convert between different data types?
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - When would you use a set instead of a list?
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - Explain how dict keys must be hashable and why.
Answer: Provide a concise explanation or implement the requested logic based on the question.
- Tricky concepts:
  - Shallow vs deep copy; default `.copy()` is shallow.
  - Mutable default arguments in functions cause shared state.
  - Float precision errors; never compare floats with `==`.
  - Strings are immutable; concatenation creates new string.
  - Dict is ordered by insertion (Python 3.7+), but not guaranteed elsewhere.
- Differences / comparisons:

| Type | Mutable | Ordered | Hashable | Use Case |
|---|---|---|---|---|
| list | Yes | Yes | No | Dynamic collections |
| tuple | No | Yes | Yes | Fixed collections, dict keys |
| set | Yes | No | No | Unique items, fast membership |
| dict | Yes | Yes (3.7+) | No | Key-value storage |
| frozenset | No | No | Yes | Immutable set, dict keys |

- Scenario-based questions:
  - Q: How would you remove duplicates from a list while preserving order?  
    A: Use `dict.fromkeys()` or list comprehension with set tracking: `seen = set(); [x for x in lst if not (x in seen or seen.add(x))]` or simpler: `list(dict.fromkeys(lst))`.
  - Q: How do you safely iterate over a dict while modifying it?  
    A: Iterate over a copy: `for key in list(d.keys()):` or `for key, value in list(d.items()):`.
- Example interview answer (mutable vs immutable):
  - Q: Why are strings immutable in Python?  
    A: Immutability enables optimization (interning, caching), thread safety (no locking needed), use as dict keys or set members (hashable), and predictable behavior. Mutable strings would require copying on every operation, reducing performance.

---

## 9. Revision Notes

- Short definitions:
  - `int`: whole numbers, arbitrary precision.
  - `float`: decimal numbers, IEEE 754, limited precision.
  - `complex`: numbers with real and imaginary parts (a + bj).
  - `bool`: True or False; subclass of int.
  - `str`: immutable text, Unicode, indexable and sliceable.
  - `list`: mutable ordered collection, supports any types.
  - `tuple`: immutable ordered collection, hashable.
  - `set`: mutable unordered collection, unique items, fast membership.
  - `dict`: mutable key-value mapping, keys must be hashable.
  - `bytes`: immutable sequence of bytes (0-255).
  - `bytearray`: mutable sequence of bytes.
  - `NoneType`: null value; single None object.
- Key syntax:
  - List: `[1, 2, 3]`; dict: `{"a": 1}`;  set: `{1, 2, 3}`; tuple: `(1, 2, 3)`
Answer: Provide a concise explanation or implement the requested logic based on the question.
  - Slice: `s[start:end:step]`
  - Type check: `type(x)`, `isinstance(x, int)`
  - Conversion: `int(x)`, `float(x)`, `str(x)`, `list(x)`
- Important rules:
  - Use `is None`, not `== None`.
  - Use `is` for identity; `==` for equality.
  - Avoid mutating mutable defaults in functions.
  - Lists and dicts are mutable; tuples and strings immutable.
- One-line explanations:
  - Slicing: `s[1:4]` includes index 1, excludes 4 (start inclusive, end exclusive).
  - Empty collections are falsy.
  - Truthiness: `0`, `""`, `None`, `False`, empty containers are falsy.

---

## 10. Practice Questions

### Theory questions
- What is the difference between mutable and immutable types?
Answer: Explain how the two concepts differ in behavior, use cases, and effect on program state.
- Why are dict keys required to be hashable?
Answer: Provide a concise explanation or implement the requested logic based on the question.
- Explain the difference between `==` (equality) and `is` (identity).
Answer: Explain how the two concepts differ in behavior, use cases, and effect on program state.
- What is the advantage of using a set over a list for membership testing?
Answer: Provide a concise explanation or implement the requested logic based on the question.
- Why should you use `isinstance()` instead of `type()`?
Answer: Provide a concise explanation or implement the requested logic based on the question.

### Coding questions
- Write a program that reads a list of numbers and removes duplicates while preserving order.
Answer: Provide a concise explanation or implement the requested logic based on the question.
- Write a function that takes a dict and returns a dict with keys and values swapped.
Answer: Follow the described algorithm and return the requested value or structure from the function.
- Create a program that counts the frequency of each character in a string using a dict.
Answer: Provide a concise explanation or implement the requested logic based on the question.
- Write a function that flattens a nested list into a single list.
Answer: Provide a concise explanation or implement the requested logic based on the question.
- Write a program that merges two dicts and handles duplicate keys.
Answer: Provide a concise explanation or implement the requested logic based on the question.

### Output prediction questions
- What is the output?
Answer: Evaluate the code example above to determine the exact output produced by the snippet.
```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```

- What is the output?
Answer: Evaluate the code example above to determine the exact output produced by the snippet.
```python
s = {3, 1, 2}
print(s)
```

- What is the output?
Answer: Evaluate the code example above to determine the exact output produced by the snippet.
```python
d = {"a": 1, "b": 2}
print(d["c"])
```

### Scenario-based questions
- How would you count how many times each word appears in a document?
Answer: Provide a concise explanation or implement the requested logic based on the question.
- How would you write a program to check if two lists contain the same elements (regardless of order)?
Answer: Provide a concise explanation or implement the requested logic based on the question.
- How would you merge multiple dicts into one?
Answer: Provide a concise explanation or implement the requested logic based on the question.

---

**Important points / Best next steps**

- Master list and dict comprehensions; they're fundamental and efficient.
- Understand mutability deeply; it's source of many bugs.
- Always use type hints; they improve code clarity and catch errors early.
- Practice type conversions and error handling for robustness.

Next, explore control flow (if/else, loops), functions, and error handling to build on this foundation.
