
ukuran = int(input())
bilangan = [int(i) for i in input().split()]

def hitungBerat ():
    total = 0
    for i in bilangan:
        total += i
    print(total)

hitungBerat()
