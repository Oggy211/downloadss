def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t

def inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def encrypt_pair(pair, key):
    a, b, c, d = key
    x, y = ord(pair[0])-65, ord(pair[1])-65
    return chr((a*x+b*y)%26+65)+chr((c*x+d*y)%26+65)

def decrypt_pair(pair, key):
    a, b, c, d = key
    det_inv = inverse((a*d-b*c)%26, 26)
    invkey = (d*det_inv%26, -b*det_inv%26, -c*det_inv%26, a*det_inv%26)
    return encrypt_pair(pair, invkey)

if __name__ == "__main__":
    key = [int(x) for x in input("Matrix a b c d: ").split()]
    if len(key) != 4:
        raise ValueError("Enter four numbers")
    message = "".join(c for c in input("Message: ").upper() if 'A' <= c <= 'Z')
    if len(message)%2:
        message += "X"
    cipher = "".join(encrypt_pair(message[i:i+2], key) for i in range(0,len(message),2))
    print("Encrypted:", cipher)
    print("Decrypted:", "".join(decrypt_pair(cipher[i:i+2],key) for i in range(0,len(cipher),2)))
