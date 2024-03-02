n = input().strip('[]')
bilangan = [int(i) for i in n.split(",")]

def jumlahNilai(bilangan):
    maks1 = 0
    maks2 = 0
    maks3 = 0
    for i in range(len(bilangan)):
        if (bilangan[i] > maks1):
            maks3 = maks2
            maks2 = maks1
            maks1 = bilangan[i]
        elif (bilangan[i] > maks2):
            maks3 = maks2
            maks2 = bilangan[i]
        elif (bilangan[i] > maks3):
            maks3 = bilangan[i]
    jumlah = maks1 + maks2 + maks3
    return jumlah

print(jumlahNilai(bilangan))