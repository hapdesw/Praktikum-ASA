x = int(input())
y = int(input())

def financialFreedom(x, y):
    uang = x
    bunga = 5/100
    for i in range(1, y+1):
        if (i >= 2):
            bunga = bunga + (0.5/100)
        uang = uang + (bunga * uang)
    return round(uang)

print(financialFreedom(x, y))