d = str(input())

def bringBoots():
    tengah = len(d) // 2
    if (len(d) % 2 == 0): 
        inisial = d[tengah-1:tengah+1]
    else:
        inisial = d[tengah]
    print("“" + inisial + "”")
    
bringBoots()