n = int(input())

jumlahGanjil = int()
for i in range(n+1):
    if i % 2 != 0:
        jumlahGanjil += i
print(jumlahGanjil)