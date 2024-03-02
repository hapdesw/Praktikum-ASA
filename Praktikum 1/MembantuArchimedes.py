
n = int(input())

def faktorBil(n):
    faktor = []
    for i in range(1, n + 1):
        if (n % i == 0):
            faktor.append(i)
    print(faktor)

faktorBil(n)


