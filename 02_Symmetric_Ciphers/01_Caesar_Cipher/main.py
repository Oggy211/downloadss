def shift_text(text, key):
    result = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch)-65+key)%26+65)
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch)-97+key)%26+97)
        else:
            result += ch
    return result

if __name__ == "__main__":
    text = input("Message: ")
    key = int(input("Shift: "))
    cipher = shift_text(text, key)
    print("Encrypted:", cipher)
    print("Decrypted:", shift_text(cipher, -key))
