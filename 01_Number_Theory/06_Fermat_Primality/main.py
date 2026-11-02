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

def fermat_test(n, bases=(2, 3, 5)):
    if n < 2:
        return False
    if n in (2, 3, 5):
        return True
    for a in bases:
        if a >= n:
            continue
        if gcd(a, n) != 1 or pow(a, n-1, n) != 1:
            return False
    return True

if __name__ == "__main__":
    n = int(input("n: "))
    print("Passes Fermat test:", fermat_test(n))
    print("Note: passing does not prove primality")
