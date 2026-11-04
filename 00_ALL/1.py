# Fermat primality test
def fermat():
    n = int(input("Enter number : "))
    a = int(input("Enter base : "))
    if n<=1:
        print("Composite")
    elif n==2 or n==3:
        print("Prime")
    elif a<=1 or a>=n:
        print("Invalid base")
    elif pow(a,n-1,n) == 1:
        print("Probable prime")
    else:
        print("Composite")

# Euler test
def jacobi(a,n):
    res = 1
    a = a%n
    while a!=0:
        while a%2==0:
            a //= 2
            if n%8==3 or n%8==5:
                res = -res
        a,n = n,a
        if a%4==3 and n%4==3:
            res = -res
        a = a%n
    if n==1:
        return res
    return 0
def euler():
    n = int(input("Enter number: "))
    a = int(input("Enter base : "))
    if n<=1 or n%2==0:
        print("Composite")
    else:
        x = pow(a,(n-1)//2,n)
        j = jacobi(a,n)%n
        if x==j:
            print("Probable prime")
        else:
            print("Composite")

# miller rabin test
def miller():
    n = int(input("Enter number : "))
    a = int(input("Enter base : "))
    if n<=1 or n%2==0:
        return "Composite"
    elif a<=1 or a>=n:
        return "Invalid"
    else:
        d = n-1
        s = 0
        while d%2==0:
            d //= 2
            s += 1
        x = pow(a,d,n)
        if x==1 or x==n-1:
            return "Probable Prime"
        for i in range(s):
            x = (x*x) % n
            if x==n-1:
                return "Probable Prime"
        return "Composite"

# Euclidean GCD
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

# Euclidean extended
def extended(a,b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while r2 != 0:
        q = r1 // r2
        r = r1 - q*r2
        s = s1 - q*s2
        t = t1 - q*t2
        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t
    return r1,s1,t1

# Euler totient function
def phi(n):
    count = 0
    for i in range(1,n):
        if gcd(i,n) == 1:
            count += 1

# Primitive root
def primitive():
    p = int(input("Enter prime : "))
    g = int(input("Enter number : "))
    if p<=2 or g<=0 or g>=p:
        return "Invalid"
    else:
        prim = True
        for i in range(1,p-1):
            if pow(g,i,p)==1:
                prim = False
                break
        if prim:
            return "Primitive"
        else:
            return "No"

# Discrete logarithm
def discrete():
    g = int(input("Enter base g: "))
    y = int(input("Enter value y: "))
    p = int(input("Enter prime p: "))
    res = -1
    val = 1
    for x in range(p):
        if val == y%p:
            res = x
            break
        val = (val * g)%p
    if res == -1:
        print("No solution")
    else:
        print("x = ",res)

# modular exponentiation
def mod_exp(a,b,m):
    result = 1
    while b>0:
        if b%2==1:
            result = (result*a) % m
        a = (a*a) % m
        b = b // 2
    return result