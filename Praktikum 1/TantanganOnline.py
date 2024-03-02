from math import isqrt

n = int(input())

def TantanganOnline(n):
    if (n <= 1 or n % 2 == 0 and (n != 2)):
        return False
    
    for i in range(3, isqrt(n)+1):
        if (n % i == 0):
            return False
        
    return True

if (TantanganOnline(n)):
    print("Prima")
else:
    print("Bukan Prima")
    


