N, M = map(int, input().split())

angka = []
for _ in range(N):
    angka.append(int(input()))

def permataSayang():
    for i in range(len(angka)):
        for j in range(len(angka)):
            if (i != j and angka[i] + angka[j] == M):
                return True
    return False
if permataSayang():
    print("I FOUND YOU!")
else:
    print("WHERE ARE YOU NOW?")