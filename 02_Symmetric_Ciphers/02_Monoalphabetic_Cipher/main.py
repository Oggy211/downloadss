ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, key):
    if len(key) != 26 or set(key) != set(ALPHABET):
        raise ValueError("Key must be a permutation of 26 uppercase letters")
    return "".join(key[ALPHABET.index(c)] if c in ALPHABET else c for c in text.upper())

def decrypt(text, key):
    return "".join(ALPHABET[key.index(c)] if c in key else c for c in text.upper())

if __name__ == "__main__":
    key = input("26-letter substitution key: ").upper()
    message = input("Message: ")
    cipher = encrypt(message, key)
    print("Encrypted:", cipher)
    print("Decrypted:", decrypt(cipher, key))
