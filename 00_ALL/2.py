# Caesar
def ceasar():
    text = input("Enter text : ").upper()
    key = int(input("Enter key : "))
    choice = input("Enter e/d : ")
    res = ""
    for ch in text:
        p = ord(ch) - 65
        if choice=="e":
            c = (p+key)%26
        else:
            c = (p-key)%26
        res += chr(c+65)
    print(res)

# monoalphabetic
def mono():
    text = input("Enter text: ").upper()
    key = input("Enter 26-letter key: ").upper()
    choice = input("Encrypt or decrypt? (e/d): ")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for ch in  text:
        if ch in alphabet:
            if choice == "e":
                result += key[ord(ch) - 65]
            else:
                result += alphabet[key.index(ch)]
        else:
            result += ch

# vigenere
def vignere():
    text = input("Enter text: ").upper()
    key = input("Enter key: ").upper()
    choice = input("Encrypt or decrypt? (e/d): ")
    result = ""
    key_length = len(key)
    key_index = 0
    for ch in text:
        if ch.isalpha():
            p = ord(ch) - 65
            k = ord(key[key_index % key_length]) - 65
            if choice == "e":
                c = (p + k) % 26
            else:
                c = (p - k) % 26
            result += chr(c + 65)
            key_index += 1
        else:
            result += ch
    print(result)

# playfair
def create_matrix(key):
    l = ""
    for ch in key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch=="J":
            ch = "I"
        if ch not in l:
            l += ch
    matrix = []
    for i in range(0,25,5):
        matrix.append(list(l[i:i+5]))
    return matrix
def prepare_text(text):
    res = ""
    i = 0
    while i<len(text):
        a = text[i]
        if i+1<len(text) and text[i]!=text[i+1]:
            b = text[i+1]
            i += 2
        else:
            b = "X"
            i += 1
        res += a+b
    return res
def find_position(matrix,ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==ch:
                return i,j
def encry(text,matrix,):
    res = ""
    for i in range(0,len(text),2):
        a = text[i]
        b = text[i+1]
        r1,c1 = find_position(matrix,a)
        r2,c2 = find_position(matrix,b)
        if r1==r2:
            res += matrix[r1][(c1+1)%5]
            res += matrix[r2][(c2+1)%5]
        elif c1==c2:
            res += matrix[(r1+1)%5][c1]
            res += matrix[(r2+1)%5][c2]
        else:
            res += matrix[r1][c2]
            res += matrix[r2][c1]
    return res
def decrypt(text, matrix):
    result = ""
    for i in range(0, len(text), 2):
        r1, c1 = find_position(matrix, text[i])
        r2, c2 = find_position(matrix, text[i+1])
        if r1 == r2:
            result += matrix[r1][(c1-1) % 5]
            result += matrix[r2][(c2-1) % 5]
        elif c1 == c2:
            result += matrix[(r1-1) % 5][c1]
            result += matrix[(r2-1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result
def playfair():
    text = input("Enter text: ").upper().replace("J","I")
    key = input("Enter key: ").upper()
    matrix = create_matrix(key)
    text = prepare_text(text)
    print("Result : ",encry(text,matrix))


# Hill Cipher
def mod_inverse(a,m):
    for i in range(1,m):
        if (a*i)%m==1:
            return i
    return -1
def det(matrix):
    n = len(matrix)
    if n==1:
        return matrix[0][0]
    elif n==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    else:
        a1 = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
        a2 = matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
        a3 = matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0]) 
        return a1-a2+a3
def encrypt_hill(text,key):
    n = len(key)
    while len(text)%n != 0:
        text += "X"
    res = ""
    for i in range(0,len(text),n):
        for r in range(n):
            total = 0
            for c in range(n):
                total += key[r][c]*(ord(text[i+c])-65)
            res += chr((total%26)+65)
    return res
def decrypt_hill(text,key):
    n = len(key)
    d = det(key)
    inv = mod_inverse(d%26,26)
    if inv == -1:
        return "Invalid key matrix"
    adj = []
    for i in range(n):
        row = []
        for j in range(n):
            b = []
            for k in range(n):
                if k != j:
                    temp = []
                    for l in range(n):
                        if l != i:
                            temp.append(key[k][l])
                    b.append(temp)
            row.append((((-1)**(i+j))*det(b)*inv)% 26)
        adj.append(row)
    return encrypt_hill(text,adj)
def hill():
    n = int(input("Enter matrix size : "))
    key = []
    print("Enter key matrix : ")
    for i in range(n):
        key.append(list(map(int,input().split())))
    text = input("Enter text: ").upper()
    if mod_inverse(det(key)%26,26)==-1:
        print("Invalid key matrix")
    else:
        cipher = encrypt_hill(text,key)
        print("Cipher text : ",cipher)
        print("Decrypted text : ",decrypt_hill(cipher,key))


# rail fence
def rail():
    text = input("Enter text: ").lower()
    rail = int(input("Enter number of rails: "))
    if rail <= 1:
        return text
    dir = 1
    row = 0
    res = [""]*rail
    for ch in text:
        res[row] += ch
        if row==0:
            dir = 1
        elif row == rail - 1:
            dir = -1
        row += dir
    print("Cipher text : ","".join(res))
def decrypt():
    text = input("Enter cipher text: ").lower()
    rail = int(input("Enter number of rails: "))
    if rail <= 1:
        print("Plain text:", text)
        return
    pattern = []
    row = 0
    dir = 1
    for ch in text:
        pattern.append(row)
        if row == 0:
            dir = 1
        elif row == rail-1:
            dir = -1
        row += dir
    res = [""] * rail
    i = 0
    for r in range(rail):
        for j in range(pattern.count(r)):
            res[r] += text[i]
            i += 1
    result = ""
    for r in pattern:
        result += res[r][0]
        res[r] = res[r][1:]
    print("Plain text:", result)

# Columnar transposition
def columnar():
    text = input("Enter text: ").upper()
    key = list(map(int,input("Enter key as space-separated numbers: ").split()))
    cols = len(key)
    while len(text) % cols != 0:
        text += "X"
    rows = len(text) // cols
    mat = []
    for i in range(rows):
        mat.append(list(text[i*cols:(i+1)*cols]))
    res = ""
    order = sorted(range(cols), key=lambda k: key[k])
    for c in order:
        for r in range(rows):
            res += mat[r][c]
    return res
def decrypt():
    text = input("Enter cipher text: ").upper()
    key = list(map(int, input("Enter key as space-separated numbers: ").split()))
    cols = len(key)
    rows = len(text) // cols
    mat = [[""] * cols for i in range(rows)]
    order = sorted(range(cols), key=lambda k: key[k])
    i = 0
    for c in order:
        for r in range(rows):
            mat[r][c] = text[i]
            i += 1
    res = ""
    for r in range(rows):
        for c in range(cols):
            res += mat[r][c]
    print("Plain text:", res.rstrip("X"))