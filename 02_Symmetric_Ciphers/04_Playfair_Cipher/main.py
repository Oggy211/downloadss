def square(key):
    letters = ""
    for c in (key + "ABCDEFGHIKLMNOPQRSTUVWXYZ").upper().replace("J", "I"):
        if 'A' <= c <= 'Z' and c not in letters:
            letters += c
    return letters

def pairs(message):
    letters = "".join(c for c in message.upper().replace("J", "I") if 'A' <= c <= 'Z')
    out = []
    i = 0
    while i < len(letters):
        a = letters[i]
        b = letters[i+1] if i+1 < len(letters) else "X"
        if a == b:
            b = "X" if a != "X" else "Q"
            i += 1
        else:
            i += 2
        out.append((a, b))
    return out

def convert(pair, grid, decrypt=False):
    a, b = pair
    ia, ib = grid.index(a), grid.index(b)
    ra, ca = divmod(ia, 5)
    rb, cb = divmod(ib, 5)
    step = -1 if decrypt else 1
    if ra == rb:
        return grid[ra*5+(ca+step)%5] + grid[rb*5+(cb+step)%5]
    if ca == cb:
        return grid[((ra+step)%5)*5+ca] + grid[((rb+step)%5)*5+cb]
    return grid[ra*5+cb] + grid[rb*5+ca]

if __name__ == "__main__":
    key = input("Key: ")
    message = input("Message: ")
    grid = square(key)
    cipher = "".join(convert(p, grid) for p in pairs(message))
    print("Encrypted:", cipher)
    print("Decrypted (includes padding):", "".join(convert((cipher[i],cipher[i+1]),grid,True) for i in range(0,len(cipher),2)))
