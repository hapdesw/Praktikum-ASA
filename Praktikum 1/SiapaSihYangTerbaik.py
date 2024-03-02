
n = input().strip('[]')
bilangan = [int(i) for i in n.split(",")]

def maksimum(bilangan):
    nilaiMaks = bilangan[0]
    for i in range(len(bilangan)):
        if (bilangan[i] >= nilaiMaks):
            nilaiMaks = bilangan[i]
    return nilaiMaks

def minimum(bilangan):
    nilaiMin = bilangan[0]
    for i in range(len(bilangan)):
        if (bilangan[i] <= nilaiMin):
            nilaiMin = bilangan[i]
    return nilaiMin

print("Nilai maksimum =", maksimum(bilangan))
print("Nilai minimum =", minimum(bilangan))