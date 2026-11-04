def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a
# RSA
def rsa():
    p = int(input("Enter prime 1: "))
    q = int(input("Enter prime 2: "))
    n = p*q
    phi = (p-1)*(q-1)
    e = print("choose e : ")
    d = pow(e,-1,phi)
    m = print("enter message(<n) : ")
    print("Public key : ",e,n)
    print("Private key : ",d,n)
    c = pow(m,e,n)
    print("Cipher : ",c)
    p = pow(c,d,n)
    print("Plain : ",p)

# ElGamal
def elgamal():
    p = int(input("Enter prime p : "))
    g = int(input("Enter root g : "))
    x = int(input("Enter private key : "))
    y = pow(g,x,p)
    print("Public key : ",y)
    m = int(input("Enter message : "))
    k = int(input("Enter random key : "))
    c1 = pow(g,k,p)
    c2 = (m*pow(y,k,p))%p
    print("Encrypted: ",c1,c2)
    s = pow(c1,x,p)
    inv = pow(s,-1,p)
    decrypt = (c2*inv)%p
    print("Decrypted: ",decrypt)

# Diffie-Hellman
def diffie():
    p = int(input("Enter prime : "))
    g = int(input("Enter g : "))
    a = int(input("Enter alice private "))
    b = int(input("Enter bob private "))
    A = pow(g,a,p)
    B = pow(g,b,p)
    print("public ",A,B)
    k1 = pow(A,b,p)
    k2 = pow(B,a,p)
    print("Shared ",k1,k2)

# ECC Elgamal
def add(P,Q,a,p):
    if P is None:
        return Q
    if Q is None:
        return P
    x1,y1 = P
    x2,y2 = Q
    if P==Q:
        m = ((3*x1*x1+a)*pow(2*y1,-1,p))%p
    else:
        m = ((y2-y1)* pow((x2-x1)%p,-1,p))%p
    x3 = (m*m-x1-x2)%p
    y3 = (m*(x1-x3)-y1)%p
    return x3,y3
def multiply(k,P,a,p):
    R = None
    while k>0:
        if k%2==1:
            R = add(R,P,a,p)
        P = add(P,P,a,p)
        k = k//2
    return R
def subtract(P,Q,a,p):
    if Q is None:
        return P
    negQ = (Q[0],(-Q[1])%p)
    return add(P,negQ,a,p)
def valid(P,a,b,p):
    if P is None:
        return False
    x,y = P
    return (y*y-x*x*x-a*x-b)%p ==0
def ecc():
    p = int(input("Enter prime : "))
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    Gx = int(input("Enter base point x ; "))
    Gy = int(input("Enter base point y : "))
    G = (Gx, Gy)
    d = int(input("Enter private key: "))
    k = int(input("Enter random key: "))
    Mx = int(input("Enter message point x: "))
    My = int(input("Enter message point y: "))  
    M = (Mx, My)
    if p <= 3 or (4*a**3 + 27*b**2) % p == 0:
        print("Invalid curve")
    elif not valid(G, a, b, p) or not valid(M, a, b, p):
        print("Invalid point")
    elif d <= 0 or k <= 0:
        print("Invalid key")
    else:
        Q = multiply(d, G, a, p)
        print("Public key:", Q)
        # Encryption
        C1 = multiply(k, G, a, p)
        temp = multiply(k, Q, a, p)
        C2 = add(M, temp, a, p)
        print("Encrypted C1:", C1)
        print("Encrypted C2:", C2)
        # Decryption
        temp = multiply(d, C1, a, p)
        decrypted = subtract(C2, temp, a, p)
        print("Decrypted message:", decrypted)