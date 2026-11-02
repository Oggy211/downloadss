def mod_power(base, exponent, modulus):
    if modulus <= 0 or exponent < 0:
        raise ValueError("Modulus must be positive; exponent nonnegative")
    result = 1 % modulus
    base %= modulus
    while exponent:
        if exponent % 2:
            result = result * base % modulus
        base = base * base % modulus
        exponent //= 2
    return result

if __name__ == "__main__":
    a = int(input("Base: "))
    b = int(input("Exponent: "))
    m = int(input("Modulus: "))
    print("Result =", mod_power(a, b, m))
