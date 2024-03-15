from math import isqrt

x = int(input())

def pasanganFaktor(x):
    faktor = []
    for i in range(1, isqrt(x)+1):
        if (x % i == 0):
            faktor.append((i, x//i))
    return faktor

print(pasanganFaktor(x))
