n = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]

def urutanSembako(n, m):
    for i in range(len(n)-1):
        if (m[i] in n and m[i+1] in n):
            a = n.index(m[i])
            b = n.index(m[i+1])
            if abs(a - b) == 1:
                return True
            else:
                return False
        
if (urutanSembako(n, m)):
    print("Ya")
else:
    print("Tidak")

