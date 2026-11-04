def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a
# RSA
def rsa():
    p = int(input("Enter p : "))
    q = int(input("Enter q : "))
    n = p*q
    phi = (p-1)*(q-1)
    e = int(input("Enter public : "))
    d = pow(e,-1,phi)
    m = int(input("Enter message : "))
    #signing
    s = pow(m,d,n)
    print("Signature : ",s)
    # verificatio
    v = pow(s,e,n)
    if v==m:
        print("Signature valid")
    else:
        print("Invalid")

# NIST DSA
def dsa():
    p = int(input("Enter p : "))
    q = int(input("Enter q : "))
    g = int(input("Enter generator : "))
    x = int(input("Enter private key : "))
    y = pow(g,x,p)
    print("Public key : ",y)
    m = int(input("Enter message : "))
    k = int(input("Enter random key : "))
    #signing
    r = pow(g,k,p)%q
    s = (pow(k,-1,q)*(m+x*r))%q
    print("Signature : ",r,s)
    #verification
    w = pow(s,-1,q)
    u1 = (m*w)%q
    u2 = (r*w)%q
    v = (pow(g,u1,p)*pow(y,u2,p))%p
    v = v%q
    if v==r:
        print("Signature valid")
    else:
        print("Invalid")


# ECDSA Digital Signature
def add(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1+y2) % p == 0:
        return None
    if P == Q:
        m = ((3*x1*x1+a) * pow(2*y1, -1, p)) % p
    else:
        m = ((y2-y1) * pow((x2-x1) % p, -1, p)) % p
    x3 = (m*m-x1-x2) % p
    y3 = (m*(x1-x3)-y1) % p
    return (x3, y3)
def multiply(k, P, a, p):
    R = None
    while k > 0:
        if k % 2 == 1:
            R = add(R, P, a, p)
        P = add(P, P, a, p)
        k = k // 2
    return R
def ecdsa():
    p = int(input("Enter prime p: "))
    a = int(input("Enter curve parameter a: "))
    b = int(input("Enter curve parameter b: "))
    Gx = int(input("Enter base point x: "))
    Gy = int(input("Enter base point y: "))
    n = int(input("Enter order of base point n: "))
    d = int(input("Enter private key d: "))
    k = int(input("Enter random key k: "))
    H = int(input("Enter message hash: "))
    G = (Gx, Gy)
    if p <= 3 or (4*a**3 + 27*b**2) % p == 0:
        print("Invalid curve")
    elif (Gy*Gy - Gx**3 - a*Gx - b) % p != 0:
        print("Invalid base point")
    elif n <= 1 or d <= 0 or d >= n or k <= 0 or k >= n:
        print("Invalid key")
    elif multiply(n, G, a, p) is not None:
        print("Invalid base point order")
    else:
        # Public key
        Q = multiply(d, G, a, p)
        print("Public key:", Q)
        # Signing
        R = multiply(k, G, a, p)
        r = R[0] % n
        if r == 0:
            print("Invalid signature")
        else:
            s = (pow(k, -1, n) * (H + d*r)) % n
            if s == 0:
                print("Invalid signature")
            else:
                print("Signature:", r, s)
                # Verification
                w = pow(s, -1, n)
                u1 = (H*w) % n
                u2 = (r*w) % n
                X = add(
                    multiply(u1, G, a, p),
                    multiply(u2, Q, a, p),
                    a, p
                )
                if X is not None and X[0] % n == r:
                    print("Signature is valid")
                else:
                    print("Invalid signature")



# ElGamal Digital Signature
def elgml():
    p = int(input("Enter prime p: "))
    g = int(input("Enter primitive root g: "))
    x = int(input("Enter private key x: "))
    if p <= 2 or g <= 1 or g >= p or x <= 0 or x >= p-1:
        print("Invalid input")
    else:
        y = pow(g, x, p)
        print("Public key:", y)
        H = int(input("Enter message hash: "))
        k = int(input("Enter random key k: "))
        if k <= 0 or k >= p-1 or gcd(k, p-1) != 1:
            print("Invalid random key")
        else:
            # Signing
            r = pow(g, k, p)
            s = (pow(k, -1, p-1) * (H-x*r)) % (p-1)
            print("Signature:", r, s)
            # Verification
            v1 = pow(g, H, p)
            v2 = (pow(y, r, p) * pow(r, s, p)) % p
            if v1 == v2:
                print("Signature is valid")
            else:
                print("Invalid signature")