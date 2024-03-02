ukuran = int(input())

bilangan = [int(i) for i in input().split()]

hitungGenap = int()
for i in bilangan:
    if i % 2 == 0:
        hitungGenap += 1
print(hitungGenap)