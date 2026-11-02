def miller_rabin(n, bases=(2, 3, 5, 7, 11)):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in bases:
        a %= n
        if a == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n-1):
            continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    print("Probably prime:", miller_rabin(int(input("n: "))))
