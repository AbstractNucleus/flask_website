from Crypto.Util import number as num
import random
import time

def gen_p():
    p = num.getPrime(16)
    while (p-1)%q != 0:
        p = num.getPrime(16)
    return p

def gen_g():
    g = 2
    while g > 1:
        g += 1
        if (g**q)%p == 1:
            return g

def gen_r():
    return ((g**k)%p)%q

def gen_i():
    i = 2
    while (k*i)%q != 1:
        i += 1
    return i

q = num.getPrime(8)
print(q)
p = gen_p()
print(p)
g = gen_g()
print(g)

x = random.randint(0, q)
y = g**x%p

message = 69
k = random.randint(0,q)
r = gen_r()
i = gen_i()
