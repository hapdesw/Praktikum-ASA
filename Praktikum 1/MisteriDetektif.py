s = str(input())

def misteriDetektif(s):
    for i in s:
        if (i == '-'):
            return True
    if (s == s[::-1]):
        return True
    else:
        return False
    
if (misteriDetektif(s)):
    print("true")
else:
    print("false")
    

