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

# Toy curve: y^2 = x^3 + ax + b (mod p). None represents point at infinity.
def on_curve(P,a,b,p):
    return P is None or (P[1]*P[1]-P[0]**3-a*P[0]-b)%p == 0

def add_points(P,Q,a,p):
    if P is None:
        return Q
    if Q is None:
        return P
    x1,y1=P
    x2,y2=Q
    if x1 == x2 and (y1+y2)%p == 0:
        return None
    if P == Q:
        slope=(3*x1*x1+a)*inverse(2*y1%p,p)%p
    else:
        slope=(y2-y1)*inverse((x2-x1)%p,p)%p
    x3=(slope*slope-x1-x2)%p
    return x3,(slope*(x1-x3)-y1)%p

def multiply(k,P,a,p):
    result=None
    while k:
        if k%2:
            result=add_points(result,P,a,p)
        P=add_points(P,P,a,p)
        k//=2
    return result

if __name__ == "__main__":
    a,b,p=2,2,17
    P=(5,1)
    print("Curve: y^2 = x^3 + 2x + 2 mod 17")
    print("Base point:",P,"on curve:",on_curve(P,a,b,p))
    print("2P:",multiply(2,P,a,p))
    print("3P:",multiply(3,P,a,p))
