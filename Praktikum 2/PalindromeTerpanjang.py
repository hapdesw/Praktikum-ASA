teks = str(input())

def palindromTerpanjang(teks):
    kata = teks.split()
    t = 0
    for i in kata:
        if (i == i[::-1]):
            if len(i) > t:
                t = len(i)
    return t
    
print(palindromTerpanjang(teks))