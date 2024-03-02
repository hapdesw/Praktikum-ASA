n = int(input())

def fikkBazz(n):
    for i in range(1, n+1):
        if (i % 3 == 0 or i % 5 == 0):
            if (i % 3 == 0 and i % 5 == 0):
                print("FikkBazz")
            elif (i % 3 == 0):
                print("Fikk")
            elif (i % 5 == 0):
                print("Bazz")
        else:
            print(i)

fikkBazz(n)