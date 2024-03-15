x = str(input())

l = [i for i in x]

k = []
for i in l:
    asciiV = ord(i)
    if (asciiV >= 110 and asciiV <= 122):
        newV = asciiV - 13
    elif (asciiV >= 97 and asciiV <= 109):
        newV = asciiV + 13
    newww = chr(newV)
    k.append(newww)
print(''.join(k))

