n = int(input())

def pedagangAyam(n):
    a = [int(i) for i in str(n)]
    i = len(a) - 1
    while i > 0:
        if (a[i] >= 5):
            a[i] = 0
            a[i-1] += 1
        else:
            a[i] = 0
        i = i - 1
    n = int(''.join(map(str, a)))
    return n
    
print(pedagangAyam(n))