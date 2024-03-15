n = int(input())
s = str(input())

k = []
def kombinasi(s, i ,n):
    if (i == n):
        k.append(" ".join(s))
    else:
        for j in range(i, n):
            s[i], s[j] = s[j], s[i]
            kombinasi(s, i+1, n)
            s[j], s[i] = s[i], s[j]

s = [char for char in s if char != " "]
kombinasi(s, 0, n)
for x in k:
    print(x)