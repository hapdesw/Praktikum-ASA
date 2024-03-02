kata = str(input())

def kamusLengkap(kata):
    for i in range(len(kata)-1):
        if (kata[i] == kata[i+1]):
            return False
    return True

if (kamusLengkap(kata)):
    print("1")
else:
    print("0")
        
kamusLengkap(kata)