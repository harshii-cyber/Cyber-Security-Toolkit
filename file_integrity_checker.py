import hashlib

filename = input("Enter file name: ")

try:
    with open(filename, "rb") as file:
        file_data = file.read()
        hash_value = hashlib.sha256(file_data).hexdigest()

    print("\nSHA-256 Hash:")
    print(hash_value)

except FileNotFoundError:
    print("File not found!")
