import hashlib

text = input("Enter text: ")

hash_value = hashlib.sha256(text.encode()).hexdigest()

print("SHA-256 Hash:")
print(hash_value)
