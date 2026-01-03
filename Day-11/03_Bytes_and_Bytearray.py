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