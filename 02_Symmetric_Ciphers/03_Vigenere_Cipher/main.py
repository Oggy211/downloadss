def transform(text, key, decrypt=False):
    key = "".join(c for c in key.upper() if 'A' <= c <= 'Z')
    if not key:
        raise ValueError("Key must contain letters")
    output = ""
    index = 0
    for c in text.upper():
        if 'A' <= c <= 'Z':
            shift = ord(key[index % len(key)]) - 65
            if decrypt:
                shift = -shift
            output += chr((ord(c)-65+shift)%26+65)
            index += 1
        else:
            output += c
    return output

if __name__ == "__main__":
    message = input("Message: ")
    key = input("Key: ")
    cipher = transform(message, key)
    print("Encrypted:", cipher)
    print("Decrypted:", transform(cipher, key, True))
