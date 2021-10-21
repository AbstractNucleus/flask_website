def encrypt(msg, n, e):
    return pow(msg, e, n)

def decrypt(cipher, n, d):
    return pow(cipher, d, n)

def hack(n, e, cipher):
    for p in range(2,n):
        if p%2 != 0:
            if n%p == 0:
                q = n/p
                break
    n = p*q
    F = (p-1)*(q-1)
    d, y, u, v, num1, num2 = 0, 1, 1, 0, e, F
    while num1 != 0:
        q, r = num2//num1, num2%num1
        num2, num1, d, y, u, v = num1, r, u, v, d-u*q, y-v*q
    if d < 0:
        d = F + d
    return int(q), int(p), int(n), int(d)

def key_gen(bits):
    from Crypto.Util import number as num
    p, q = num.getStrongPrime(bits), num.getStrongPrime(bits)
    F, n, e = (p-1)*(q-1), p * q, 2**16+1
    d, y, u, v, num1, num2 = 0, 1, 1, 0, e, F
    while num1 != 0:
        o, r = num2//num1, num2%num1
        num2, num1, d, y, u, v = num1, r, u, v, d-u*o, y-v*o
    if d < 0:
        d = F + d
    return p, q, F, n, e, d

