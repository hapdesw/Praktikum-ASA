X = int(input())
Y = [int(i) for i in input().split()]

def cariTarget():
    hitung = 0
    for i in range(len(Y)):
        for j in range(i+1, len(Y)):
            if (i != j and Y[i] + Y[j] == X):
                hitung += 1
                print(i, j) 
                break
    if (hitung == 0):
        print("-")
cariTarget()
            