n = int(input())

def bintangTerbalik(n):
    count = n + 1;
    while count > 1:
        hasil = "*" * n
        print(hasil)
        n -= 1
        count -= 1

bintangTerbalik(n)