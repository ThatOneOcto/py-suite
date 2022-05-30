import base64

print("Welcome to the simple base64 encode and decoder")
en_or_de = input("Do you want to encode or decode in base64? (en/de) ")
if en_or_de.lower() == "en":
    message = input("What do you want to encode in base64? ")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print(base64_message)
else:
    base64_message = input("What do you want to decode in base64? ")
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    print(message)
