n = int(input())

def fibonacci(n):
    a = 0
    b = 1
    count = 0
    fibo = []
    while count < n:
        fibo.append(a)
        baru = a + b
        a = b
        b = baru
        count += 1
    print(fibo)

fibonacci(n)