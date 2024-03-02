n = int(input())

def segitigaAjaib():
    segitiga = []
    for i in range(1, n+1):
        a = []
        s = 1
        for j in range(1, i+1):
            a.append(s)
            s = s * (i - j) // j 
        segitiga.append(a)
    print(segitiga)

segitigaAjaib()