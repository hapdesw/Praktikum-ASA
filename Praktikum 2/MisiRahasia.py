n = int(input())

def misiRahasia(n):
    alfabet = []
    for i in range(1, 27):
        asc = chr(i + 96)
        alfabet.append(asc)
    
    if (n >= 1 and n <= 26):
        return alfabet[0] + alfabet[0] + alfabet[(n-3) % 26]
    elif (n >= 27 and n <= 52):
        return alfabet[0] + alfabet[(n-28) % 26] + alfabet[25]
    elif (n >= 52 and n <= 79):
        return alfabet[(n-53) % 26] + alfabet[25] + alfabet[25]

print(misiRahasia(n))
