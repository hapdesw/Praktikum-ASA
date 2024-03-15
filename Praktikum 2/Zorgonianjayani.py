s = str(input())

def zorgon(s):
    maks = 0
    c = 1
    for i in range(1, len(s)):
        if (s[i] == s[i-1]):
            c += 1
        else:
            if (c > maks):
                maks = c
            c = 1
    if (c > maks):
        maks = c
    return maks

print(zorgon(s))