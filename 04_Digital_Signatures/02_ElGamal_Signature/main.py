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

# Toy ElGamal signature; fixed parameters for demonstration only.
def sign(m,p,g,x,k):
    r=pow(g,k,p)
    s=((m-x*r)*inverse(k,p-1))%(p-1)
    return r,s

def verify(m,p,g,y,r,s):
    return 0<r<p and 0<=s<p-1 and pow(g,m,p)==(pow(y,r,p)*pow(r,s,p))%p

if __name__ == "__main__":
    p,g,x,k=23,5,6,7
    m=int(input("Message integer: "))
    y=pow(g,x,p)
    r,s=sign(m,p,g,x,k)
    print("Signature:",(r,s))
    print("Verified:",verify(m,p,g,y,r,s))
    print("Tampered verified:",verify(m+1,p,g,y,r,s))
