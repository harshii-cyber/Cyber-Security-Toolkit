url = input("Enter URL: ")

if url.startswith("https://"):
    print("Secure URL (HTTPS)")
else:
    print("Not Secure (HTTP)")
