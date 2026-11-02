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

# Educational textbook RSA signature: NOT RSA-PSS and not secure.
def sign(message,d,n):
    return pow(message,d,n)

def verify(message,signature,e,n):
    return pow(signature,e,n)==message%n

if __name__ == "__main__":
    p,q,e=11,17,7
    n=p*q
    d=inverse(e,(p-1)*(q-1))
    message=int(input("Message integer: "))
    if not 0 <= message < n:
        raise ValueError("Message out of range")
    signature=sign(message,d,n)
    print("Signature:",signature)
    print("Verified:",verify(message,signature,e,n))
    print("Tampered message verified:",verify((message+1)%n,signature,e,n))
