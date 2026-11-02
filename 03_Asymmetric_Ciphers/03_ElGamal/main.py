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

if __name__ == "__main__":
    p = int(input("Prime p: "))
    g = int(input("Generator g: "))
    x = int(input("Private key x: "))
    k = int(input("Ephemeral key k: "))
    m = int(input("Message integer 1..p-1: "))
    if not is_prime(p) or not (1 <= x < p-1 and 1 <= k < p-1 and 1 <= m < p):
        raise ValueError("Invalid toy ElGamal parameters")
    y = pow(g,x,p)
    c1 = pow(g,k,p)
    c2 = m*pow(y,k,p)%p
    shared = pow(c1,x,p)
    recovered = c2*inverse(shared,p)%p
    print("Public key:", (p,g,y))
    print("Ciphertext:", (c1,c2), "Decrypted:", recovered)
