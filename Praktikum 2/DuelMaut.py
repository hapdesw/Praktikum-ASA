a, b = map(int, input().split())

def duelMaut(a, b):
    menang = 0
    kalah = 0
    seri = 0
    for i in range(1, 7):
        jarakA = abs(a - i)
        jarakB = abs(b - i)
        if jarakA < jarakB:
            menang = menang + 1
        elif jarakA > jarakB:
            kalah = kalah + 1
        else:
            seri = seri +1
    hasil = menang, seri, kalah
    hasil2 = ' '.join(map(str, hasil))
    return hasil2


print(duelMaut(a, b))
