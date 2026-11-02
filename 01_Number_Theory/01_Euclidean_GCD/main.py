def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

if __name__ == "__main__":
    a = int(input("First integer: "))
    b = int(input("Second integer: "))
    print("GCD =", gcd(a, b))
