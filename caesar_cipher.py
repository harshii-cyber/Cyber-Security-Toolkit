text = input("Enter text: ")
shift = int(input("Enter shift value: "))

result = ""

for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char) - start + shift) % 26 + start)
    else:
        result += char

print("Encrypted Text:", result)
