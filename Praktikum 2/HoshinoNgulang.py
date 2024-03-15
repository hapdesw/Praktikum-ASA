text1 = str(input())
text2 = str(input())

def hoshinoNgulang(text1, text2, x, y, m={}):
    if (x, y) in m:
        return m[(x, y)]
    elif x == len(text1) or y == len(text2):
        return ""
    elif text1[x] == text2[y]:
        hasil = text1[x] + hoshinoNgulang(text1, text2, x + 1, y + 1, m)
    else:
        hasil = max(hoshinoNgulang(text1, text2, x + 1, y, m), hoshinoNgulang(text1, text2, x, y + 1, m), key = len)
    m[(x, y)] = hasil
    return hasil

print(hoshinoNgulang(text1, text2, 0, 0))
