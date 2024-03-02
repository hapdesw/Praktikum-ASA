n = int(input())

def fibonacci(n):
    if (n == 0):
        print("0")
    elif (n == 1):
        print("1")
    else:
        a = 0
        b = 1
        for _ in range(2, n+1):
            baru = b
            b = a + b
            a = baru
        return b

print(fibonacci(n))